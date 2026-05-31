from openai import OpenAI

client = OpenAI(
    base_url="http://10.42.208.168:8083/mimik-ai/openai/v1",
    api_key="1234"
)

response = client.chat.completions.create(
    model="qwen3-1.7b",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)