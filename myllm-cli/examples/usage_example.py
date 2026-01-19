"""
Example: Using MyLLM API Server with Python
"""

import requests
import json

# Server configuration
BASE_URL = "http://localhost:8080/v1"

def list_models():
    """List available models"""
    response = requests.get(f"{BASE_URL}/models")
    return response.json()

def chat_completion(model_name, messages, temperature=0.7, max_tokens=512):
    """Send a chat completion request"""
    payload = {
        "model": model_name,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    return response.json()

def text_completion(model_name, prompt, temperature=0.7, max_tokens=512):
    """Send a text completion request"""
    payload = {
        "model": model_name,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    response = requests.post(
        f"{BASE_URL}/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    return response.json()

def main():
    """Example usage"""

    # List available models
    print("Available models:")
    models = list_models()
    for model in models.get("data", []):
        print(f"  - {model['id']}")

    if not models.get("data"):
        print("No models loaded. Please load a model first:")
        print("  myllm load <model-name>")
        return

    # Use the first available model
    model_name = models["data"][0]["id"]
    print(f"\nUsing model: {model_name}\n")

    # Example 1: Chat completion
    print("=" * 50)
    print("Example 1: Chat Completion")
    print("=" * 50)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    response = chat_completion(model_name, messages)
    assistant_message = response["choices"][0]["message"]["content"]

    print(f"User: {messages[1]['content']}")
    print(f"Assistant: {assistant_message}")
    print()

    # Example 2: Text completion
    print("=" * 50)
    print("Example 2: Text Completion")
    print("=" * 50)

    prompt = "Once upon a time, in a land far away,"
    response = text_completion(model_name, prompt)
    completion = response["choices"][0]["text"]

    print(f"Prompt: {prompt}")
    print(f"Completion: {completion}")
    print()

    # Example 3: Multi-turn conversation
    print("=" * 50)
    print("Example 3: Multi-turn Conversation")
    print("=" * 50)

    conversation = [
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Write a Python function to calculate factorial"}
    ]

    response = chat_completion(model_name, conversation)
    assistant_reply = response["choices"][0]["message"]["content"]

    print(f"User: {conversation[1]['content']}")
    print(f"Assistant: {assistant_reply}")
    print()

    # Continue the conversation
    conversation.append({"role": "assistant", "content": assistant_reply})
    conversation.append({"role": "user", "content": "Now add error handling to it"})

    response = chat_completion(model_name, conversation)
    assistant_reply = response["choices"][0]["message"]["content"]

    print(f"User: {conversation[3]['content']}")
    print(f"Assistant: {assistant_reply}")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the server.")
        print("Make sure the server is running:")
        print("  myllm server start")
    except Exception as e:
        print(f"Error: {e}")
