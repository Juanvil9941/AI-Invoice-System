from services.llm_router import route_llm
import re

async def extraction_agent(text):

    invoice_number = None
    po_number = None
    amount = None
    vendor = None

    invoice_match = re.search(r"Invoice Number:\s*(\S+)", text)
    if invoice_match:
        invoice_number = invoice_match.group(1)

    po_match = re.search(r"Purchase Order:\s*(\S+)", text)
    if po_match:
        po_number = po_match.group(1)

    amount_match = re.search(r"Amount:\s*(\d+)", text)
    if amount_match:
        amount = int(amount_match.group(1))

    vendor_match = re.search(r"Vendor:\s*(.*)", text)
    if vendor_match:
        vendor = vendor_match.group(1).strip()

    return {
        "invoice_number": invoice_number,
        "po_number": po_number,
        "amount": amount,
        "vendor": vendor
    }