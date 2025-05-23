import ollama

def get_ollama_response(user_input, file_context=None):
    base_prompt = "You are a helpful assistant."
    if file_context:
        base_prompt += f"\n\nHere is the uploaded file content to consider:\n{file_context}"

    full_prompt = f"{base_prompt}\n\nUser: {user_input}\nAssistant:"
    
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response['message']['content']
