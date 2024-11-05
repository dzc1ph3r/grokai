import requests


user_content = input("Enter your prompt: ")

url = "https://api.x.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "  # Your API from https://console.x.ai/
}
data = {
    "messages": [
        {
            "role": "system",
            "content": "You are a Grok."
        },
        {
            "role": "user",
            "content": user_content  
        }
    ],
    "model": "grok-beta",
    "stream": False,
    "temperature": 0
}

response = requests.post(url, headers=headers, json=data)


content = response.json().get("choices", [{}])[0].get("message", {}).get("content")
print(content)

