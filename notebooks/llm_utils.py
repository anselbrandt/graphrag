from openai import OpenAI

BASE_URL = "https://mlkyway.anselbrandt.net/llama/v1"
model = "Mistral-7B-Instruct-v0.3.Q8_0.gguf"

openai_api_key = "EMPTY"
openai_api_base = BASE_URL

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)


def ask_llm(context, model=model):
    data = {
        "model": model,
        "max_tokens": 1000,
        "temperature": 0,
        "messages": [
            {"role": "user", "content": context},
        ],
    }
    response = client.chat.completions.create(**data)
    chat_response = response.choices[0].message.content
    return chat_response
