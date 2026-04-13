import re
from services.llm_service import ask_llm_async
from utils.response_parser import parse_llm_response

async def fraud_agent(data):

    amount = data.get("amount")
    vendor = data.get("vendor")
    invoice_number = data.get("invoice_number")

    issues = []

    if not invoice_number:
        issues.append("Missing invoice number")

    if amount and amount > 100000:
        issues.append("Amount too high")

    if vendor and len(vendor) < 3:
        issues.append("Vendor suspicious")

    if issues:
        return {
            "agent": "fraud",
            "status": "fail",
            "reason": ", ".join(issues)
        }

    return {
        "agent": "fraud",
        "status": "pass",
        "reason": ""
    }