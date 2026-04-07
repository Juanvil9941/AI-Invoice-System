import json
import re

def parse_llm_response(response: str):

    try:
        json_text = re.search(r'\{.*\}', response, re.DOTALL).group()
        result = json.loads(json_text)

        status = result.get("status", "").lower()

        
        if status in ["pass", "success", "ok"]:
            status = "pass"
        else:
            status = "fail"

        return {
            "status": status,
            "reason": result.get("reason", "")
        }

    except:
        return {
            "status": "fail",
            "reason": "Invalid LLM response"
        }