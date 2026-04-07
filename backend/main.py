from fastapi import FastAPI, UploadFile, File
from backend.controllers.invoice_controller import router as invoice_router
from backend.services.vector_db_service import init_collection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 👈 important
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_collection(384)

app.include_router(invoice_router)