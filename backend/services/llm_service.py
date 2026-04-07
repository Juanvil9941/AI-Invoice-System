import requests
import asyncio


def ask_llm(prompt: str):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        print("Ollama Error:", str(e))
        return '{"status": "fail", "reason": "Ollama not responding"}'



async def ask_llm_async(prompt: str):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, ask_llm, prompt)