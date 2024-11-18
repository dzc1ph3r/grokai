import requests

def send_xai_request(user_prompt):
    url = "https://api.x.ai/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer xai-fj7XRGBuxikWQJ5t6XIY7R3t2rUKVewpO3QAkZZDSqsGJESiWikVFmfW4vb87D5OwoHwmLkpzCzns8xG"
    }
    
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a test assistant."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "model": "grok-beta",
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    while True:
        user_prompt = input("\nEnter your prompt (or 'quit' to exit): ")
        
        if user_prompt.lower() == 'quit':
            break
        
        response = send_xai_request(user_prompt)
        print(response)

if __name__ == "__main__":
    main()
