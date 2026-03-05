# 1. Get the environment ready, import anthropic loads the Claude library

import anthropic
import os

# 2. Read and Validate the API key, load_dotenv() reads the file .env where you saved the API key, os.getenv("ANTHROPIC_API_KEY") gets the key from the environment variables.
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv(dotenv_path=".env", override=True)

# If the key doesn't exist, the program stops inmediatly to avoid errors
api_key=os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError(
        "ANTRHOPIC_API_KEY is not defined."
        "Verify that the file .env exists and it's properly set."
    )

# 3. Initialize the Anthropic client, this connexion with Claude will be reused for all the next calls

client = anthropic.Anthropic(api_key=api_key)

# Create message
conversation = []

while True: 
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Chat ended. Sayonara")
        break

    # Add user message to the conversation
    conversation.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        messages=conversation
    )

    bot_message = response.content[0].text
    print(f"Claude: {bot_message}")

    # Add chatbot message to the conversation
    conversation.append({"role": "user", "content": user_message})