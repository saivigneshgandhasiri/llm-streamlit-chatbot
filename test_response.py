from ollama import Client

client = Client(host='http://localhost:11434')  # Default Ollama host

response = client.chat(
    model='llama3',
    messages=[
        {"role": "user", "content": "Write a short motivational message for job seekers."}
    ]
)

print(response['message']['content'])
