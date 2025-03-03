from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
OPENAI_API_KEY = os.getenv()
if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set 'OPENAI_API_KEY' in your environment variables.")

openai.api_key = OPENAI_API_KEY

# Initialize FastAPI app
app = FastAPI()

# Define request model
class ChatRequest(BaseModel):
    user_message: str

# Define API route for chatbot interaction
@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": request.user_message}]
        )

        ai_response = response["choices"][0]["message"]["content"]

        return {"status": "success", "ai_response": ai_response}

    except openai.error.AuthenticationError:
        raise HTTPException(status_code=401, detail="❌ Invalid OpenAI API Key")
    
    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"🛑 OpenAI API Error: {str(e)}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"🚨 Internal Server Error: {str(e)}")
