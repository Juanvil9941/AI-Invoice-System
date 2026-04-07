from langchain.llms import Ollama
import os

USE_LLM = os.getenv("USE_LLM", "true").lower() == "true"

llm = Ollama(model="llama3")

def rag_decision(current_invoice_text, similar_invoices):

    # Build simple context (you already do something like this)
    context = ""
    for inv in similar_invoices:
        context += f"Decision: {inv['payload'].get('decision')}\n"

    if USE_LLM:
        try:
            response = chain.run({
                "invoice": current_invoice_text,
                "context": context
            })

            import json
            return json.loads(response)

        except Exception as e:
            print(" LLM failed, switching to fallback:", e)

    # FALLBACK LOGIC
    if similar_invoices:
        hold_count = sum(
            1 for r in similar_invoices
            if r.payload.get("decision") == "HOLD"
        )

        total = len(similar_invoices)

        decision = "HOLD" if hold_count > total / 2 else "APPROVE"
        confidence = round(hold_count / total, 2)

    else:
        decision = "APPROVE"
        confidence = 0.7

    return {
        "decision": decision,
        "confidence": confidence,
        "reason": "Fallback decision based on similar invoices",
        "evidence": []
    }