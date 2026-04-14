from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You must return only valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI Error:", str(e))
        return '{"status": "fail", "reason": "OpenAI error"}'


async def ask_llm_async(prompt: str):
    return ask_llm(prompt)