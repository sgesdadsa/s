"""
Example: Using MyLLM API Server with OpenAI Python SDK

Install OpenAI SDK first:
    pip install openai
"""

from openai import OpenAI

# Initialize client pointing to your local server
client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="not-needed"  # API key not required for local server
)

def list_models():
    """List available models"""
    models = client.models.list()
    print("Available models:")
    for model in models.data:
        print(f"  - {model.id}")
    return models.data

def chat_example(model_name):
    """Chat completion example"""
    print(f"\n{'='*50}")
    print("Chat Completion Example")
    print('='*50)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain quantum computing in simple terms."}
        ],
        temperature=0.7,
        max_tokens=256
    )

    print(f"User: Explain quantum computing in simple terms.")
    print(f"Assistant: {response.choices[0].message.content}")
    print(f"\nTokens used: {response.usage.total_tokens}")

def streaming_chat_example(model_name):
    """Streaming chat example"""
    print(f"\n{'='*50}")
    print("Streaming Chat Example")
    print('='*50)

    print("User: Write a short poem about coding.")
    print("Assistant: ", end="", flush=True)

    stream = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": "Write a short poem about coding."}
        ],
        temperature=0.9,
        max_tokens=128,
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print("\n")

def function_calling_example(model_name):
    """Example with function calling (if supported)"""
    print(f"\n{'='*50}")
    print("Conversation Example")
    print('='*50)

    messages = [
        {"role": "system", "content": "You are a helpful coding tutor."},
        {"role": "user", "content": "What is a list comprehension in Python?"}
    ]

    # First response
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
        max_tokens=200
    )

    assistant_message = response.choices[0].message.content
    print(f"User: {messages[1]['content']}")
    print(f"Assistant: {assistant_message}")

    # Continue conversation
    messages.append({"role": "assistant", "content": assistant_message})
    messages.append({"role": "user", "content": "Can you show me an example?"})

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
        max_tokens=200
    )

    print(f"\nUser: {messages[3]['content']}")
    print(f"Assistant: {response.choices[0].message.content}")

def main():
    """Run examples"""
    try:
        # List models
        models = list_models()

        if not models:
            print("\nNo models loaded. Please load a model first:")
            print("  myllm load <model-name>")
            return

        # Use first available model
        model_name = models[0].id
        print(f"\nUsing model: {model_name}")

        # Run examples
        chat_example(model_name)

        # Uncomment to try streaming (if supported)
        # streaming_chat_example(model_name)

        function_calling_example(model_name)

    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure:")
        print("  1. The server is running: myllm server start")
        print("  2. At least one model is loaded: myllm load <model-name>")

if __name__ == "__main__":
    main()
