from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    user_message: str

@app.post("/chat")  # ✅ Ensure this matches your Postman request method
async def chat(request: ChatRequest):
    return {"response": f"Chatbot received: {request.user_message}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
