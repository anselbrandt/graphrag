from openai import OpenAI

BASE_URL = "https://mlkyway.anselbrandt.net/ollama/v1"

openai_api_key = "EMPTY"
openai_api_base = BASE_URL

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)


def ask_llm(context, model, tokens):
    data = {
        "model": model,
        "max_tokens": tokens,
        "temperature": 0,
        "messages": [
            {"role": "user", "content": context},
        ],
    }
    response = client.chat.completions.create(**data)
    chat_response = response.choices[0].message.content.replace("\n\n", "\n")
    return chat_response
