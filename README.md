# 🚀 AI-Powered Invoice Processing System

## 🧠 Overview

This project is a **Full-stack AI invoice processing system** that combines OCR, rule-based validation, and a Retrieval-Augmented Generation (RAG) pipeline to automate invoice verification.

The system extracts data from PDF invoices, validates them using multiple agents, retrieves similar historical invoices using vector embeddings, and generates intelligent approval decisions.

---

## ✨ Key Features

* 📄 PDF Invoice Processing (OCR + text extraction)
* 🤖 Multi-Agent Validation System

  * Invoice Validation Agent
  * Purchase Order (PO) Agent
  * Fraud Detection Agent
* 🧠 RAG-based Decision Engine (Qdrant + Embeddings)
* 🔍 Semantic Search for Similar Invoices
* 📊 Confidence-based Decision Making
* 💾 MongoDB Storage for Invoice History
* 🌐 Full-stack UI with Next.js + Tailwind CSS

---


## 🏗️ Architecture

```text
User Upload (PDF)
        ↓
Text Extraction (OCR / pdfplumber)
        ↓
Agent Validation (Invoice / PO / Fraud)
        ↓
Embedding Generation (Sentence Transformers)
        ↓
Vector Search (Qdrant)
        ↓
RAG Decision Engine (LLM)
        ↓
Store in MongoDB
        ↓
Display in UI (Next.js Dashboard)
```
---
## 📂 Project Structure

```
invoice-ai-system/
│
├── backend/
│   ├── controllers/
│   │   └── invoice_controller.py      # API endpoints (main processing logic)
│   │
│   ├── services/
│   │   ├── rag_service.py             # RAG + LLM + fallback logic
│   │   ├── vector_db_service.py       # Qdrant operations (store/search)
│   │   ├── embedding_service.py       # Generate embeddings
│   │   ├── ocr_service.py             # PDF text extraction (OCR/pdfplumber)
│   │   └── db_service.py              # MongoDB operations
│   │
│   ├── db/
│   │   └── mongo.py                   # MongoDB connection
│   │
│   ├── main.py                        # FastAPI app entry point
│   ├── requirements.txt               # Python dependencies
│   └── .env                           # Environment variables (USE_LLM)
│
├── frontend/
│   ├── app/
│   │   └── page.tsx                   # Main UI page
│   │
│   ├── components/
│   │   ├── invoice-uploader.tsx       # Upload PDF component
│   │   ├── results-panel.tsx          # Shows results (decision, agents, similarity)
│   │   └── invoice-history.tsx        # Displays past invoices
│   │
│   ├── lib/
│   │   └── api.ts                     # API calls to backend
│   │
│   ├── types/
│   │   └── invoice.ts                 # TypeScript interfaces
│   │
│   ├── package.json                  # Frontend dependencies
│   └── tsconfig.json                 # TypeScript configuration
│
├── sample_invoices/                  # Test PDFs (pass/hold/fail)
│
├── README.md                        # Project documentation
└── .gitignore
```

---

## 🛠️ Tech Stack

### 🔹 Backend

* FastAPI (Python)
* pdfplumber / Tesseract (OCR)
* REST APIs

### 🔹 AI / ML

* Ollama (Local LLM)
* Sentence Transformers (Embeddings)
* Qdrant (Vector Database)
* RAG (Retrieval-Augmented Generation)

### 🔹 Frontend

* Next.js (TypeScript)
* Tailwind CSS

### 🔹 Database

* MongoDB

---

## 🧪 How It Works

1. Upload a PDF invoice through the UI
2. System extracts text from the document
3. Multiple agents validate invoice fields
4. Embeddings are generated for the invoice
5. Similar invoices are retrieved from Qdrant
6. RAG pipeline generates a decision
7. Results are stored and displayed in UI

---

## 📊 Sample Output

```json
{
  "decision": "HOLD",
  "confidence": 0.87,
  "agent_results": [
    { "agent": "invoice", "status": "pass" },
    { "agent": "po", "status": "pass" },
    { "agent": "fraud", "status": "fail" }
  ],
  "similar_invoices": [
    {
      "score": 0.92,
      "decision": "HOLD"
    }
  ]
}
```

---

## ⚙️ Setup Instructions

### 🔧 Backend Setup

```bash
git clone <your-repo-url>
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 🌐 Frontend Setup

```bash
cd frontend

npm install
npm run dev
```

Frontend URL:

```
http://localhost:3000
```

---

## 🔑 Environment Variables

Create a `.env` file in backend:

```env
USE_LLM=true
```

* `true` → Uses local LLM (Ollama)
* `false` → Uses fallback logic (for deployment)

---

pip install -r requirements.txt

---

## 🚀 Future Improvements

* 🔹 LangChain integration for RAG pipeline
* 🔹 Multi-invoice PDF splitting
* 🔹 Cloud deployment (Vercel + Render)
* 🔹 Advanced fraud detection models
* 🔹 Real-time monitoring dashboard

---

## 💡 Key Highlights

* Built a **full-stack AI system** end-to-end
* Implemented **RAG architecture with vector search**
* Designed **multi-agent validation pipeline**
* Integrated **semantic similarity for decision support**
* Developed **interactive UI dashboard**

---

## 📸 Screenshots
![alt text](<Screenshot 2026-04-06 235517.png>) ![alt text](<Screenshot 2026-04-06 235445.png>) ![alt text](<Screenshot 2026-04-06 235304.png>)


---

## 📌 Conclusion

This project demonstrates how AI, vector search, and modern web technologies can be combined to build a scalable, intelligent invoice processing system with real-world applications in finance and automation.

---

## 🙌 Author

Sai Dari

---
