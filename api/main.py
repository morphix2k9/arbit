from fastapi import FastAPI
from api.chatbot import chatbot_response  # Import chatbot logic

app = FastAPI()

@app.get("/chat")
async def chat():
    return chatbot_response()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
