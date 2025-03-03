import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("❌ OpenAI API Key is missing. Set 'OPENAI_API_KEY' in your .env file.")
    exit(1)

openai.api_key = OPENAI_API_KEY

# Test the OpenAI API Key
try:
    response = openai.models.list()
    models = [model.id for model in response["data"]]
    print("✅ OpenAI API Key is valid. Available models:")
    for model in models:
        print(f" - {model}")
except openai.error.AuthenticationError:
    print("❌ Invalid OpenAI API Key. Please check your .env file.")
except openai.error.OpenAIError as e:
    print(f"🛑 OpenAI API Error: {str(e)}")
except Exception as e:
    print(f"🚨 Unexpected Error: {str(e)}")
