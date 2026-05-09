import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")


def build_prompt(context):
    return f"""
You are an expert compliance auditor.

Analyze the following company policy and identify:

1. Potential risks
2. Missing clauses
3. Ambiguous statements

For each issue:
- Explain the problem
- Suggest an improvement

Return output in this format:

Risks:
- ...

Missing Clauses:
- ...

Ambiguities:
- ...

Policy:
{context}
"""


# 🔹 OLLAMA (LOCAL)
def ollama_response(prompt):
    import requests

    model = os.getenv("OLLAMA_MODEL", "gemma:2b")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# 🔹 GROQ (API)
def groq_response(prompt):
    from groq import Groq

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# MAIN FUNCTION (UNIFIED)
def get_llm_response(context):

    prompt = build_prompt(context)

    if LLM_PROVIDER == "ollama":
        return ollama_response(prompt)

    elif LLM_PROVIDER == "groq":
        return groq_response(prompt)

    else:
        return "Invalid LLM provider"
