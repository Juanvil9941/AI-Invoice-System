import re
from backend.services.llm_service import ask_llm_async
from backend.utils.response_parser import parse_llm_response

async def invoice_agent(data):

    if not re.search(r"Invoice Number", data):
        return {
            "agent": "invoice",
            "status": "fail",
            "reason": "Missing invoice number"
        }


    prompt = f"""
    Validate invoice format.

    STRICT RULES:
    - Respond ONLY in JSON
    - No explanation
    - Format:
    {{ "status": "pass or fail", "reason": "..." }}

    Invoice:
    {data}
    """

    response = await ask_llm_async(prompt)
    result = parse_llm_response(response)

    return {
        "agent": "invoice",
        **result
    }