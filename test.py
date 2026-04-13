from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:11434/v1",
)
completion = client.chat.completions.create(
    model="qwen3:8b",
    messages=[
        {"role": "user", "content": "你是谁？你能做什么？"},
        {"role": "system", "content": "you are a professional assistant in the field of software development."},
        {"role": "user", "content": "你是谁？你能做什么？"},
    ],
    stream=True
)
for chunk in completion:
    print(chunk.choices[0].delta.content, end=" ",flush=True)