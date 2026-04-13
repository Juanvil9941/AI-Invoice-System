from fastapi import APIRouter, UploadFile, File
from services.embedding_service import generate_embedding
from services.chroma_service import store_embedding_data, search_similar_data
from agents.extraction_agent import extraction_agent

import asyncio
import os
import tempfile
import traceback

# Agents
from agents.invoice_agent import invoice_agent
from agents.po_agent import po_agent
from agents.fraud_agent import fraud_agent

# Services
from services.db_service import save_invoice, get_all_invoices

# Utils
from utils.pdf_extractor import extract_text

router = APIRouter()


@router.post("/process-invoice")
async def process_invoice(file: UploadFile = File(...)):
    try:
        print("Received file:", file.filename)

        if file.content_type != "application/pdf" or not file.filename.endswith(".pdf"):
            return {"error": "Only PDF files are allowed"}

        contents = await file.read()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(contents)
            temp_file_path = temp_file.name

        try:
            print("Extracting text")
            text = extract_text(temp_file_path)
            print("Extracted text length:", len(text))

        
            extracted_data = await extraction_agent(text)

          
            print("Running agents")
            results = await asyncio.gather(
                invoice_agent(extracted_data),
                po_agent(extracted_data),
                fraud_agent(extracted_data),
                return_exceptions=True
            )

            
            processed_results = []
            for r in results:
                if isinstance(r, Exception):
                    print("Agent error:", str(r))
                    processed_results.append({
                        "agent": "unknown",
                        "status": "fail",
                        "reason": str(r)
                    })
                else:
                    processed_results.append(r)

            results = processed_results

            
            decision = {
                "decision": "HOLD" if any(r["status"] == "fail" for r in results) else "APPROVE",
                "issues": [r for r in results if r["status"] == "fail"]
            }

            
            try:
                embedding = generate_embedding(text)

                similar = search_similar_data(embedding)

                if not similar:
                    similar = {"documents": [[]]}

                similar_texts = similar.get("documents", [[]])[0]

                is_duplicate = False
                for s in similar_texts:
                    if text[:100] in s:
                        is_duplicate =  True
                        break

            except Exception as e:
                print("Similarity failed:", str(e))
                similar_texts = []
                is_duplicate = False

           
            invoice_data = {
                "text": text,
                "extracted_data": extracted_data,
                "agent_results": results,
                "final_decision": decision
            }

            save_invoice(invoice_data)

           
            return {
             "summary": {
               "decision": decision["decision"],
               "duplicate_detected": is_duplicate
     },
       "text_preview": text[:150] if text else "",
       "invoice": extracted_data,
       "validation": results,
        "similar_invoices": similar_texts
            }

        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

    except Exception as e:
        print("ERROR OCCURRED:")
        traceback.print_exc()

        return {
        "summary": {
        "decision": decision["decision"],
        "issues_count": len(decision["issues"])
        },
        "invoice": extracted_data,
        "validation": results,
        "similar_invoices": similar_texts
    }


@router.get("/invoices")
def fetch_invoices():
    return get_all_invoices()