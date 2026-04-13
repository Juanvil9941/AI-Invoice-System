from services.llm_service import ask_llm_async
import json

import re

async def po_agent(data):

   po_number = data.get("po_number")

   if po_number:
        return {
            "agent": "po",
            "status": "pass",
            "reason": ""
        }

   return {
        "agent": "po",
        "status": "fail",
        "reason": "Purchase Order not found"
    }