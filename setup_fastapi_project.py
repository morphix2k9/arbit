import os

# Define the target directory and file paths
base_dir = r"C:\Wrkspace\ai-arbitrage\api"
main_file = os.path.join(base_dir, "main.py")
chatbot_file = os.path.join(base_dir, "chatbot.py")
init_file = os.path.join(base_dir, "__init__.py")

# Ensure the directory exists
os.makedirs(base_dir, exist_ok=True)

# FastAPI main.py script
main_script = """\
from fastapi import FastAPI
from api.chatbot import chatbot_response  # Import chatbot logic

app = FastAPI()

@app.get("/chat")
async def chat():
    return chatbot_response()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
"""

# chatbot.py script
chatbot_script = """\
def chatbot_response():
    return {"message": "Chatbot is working!"}
"""

# Write scripts to files
with open(main_file, "w", encoding="utf-8") as f:
    f.write(main_script)

with open(chatbot_file, "w", encoding="utf-8") as f:
    f.write(chatbot_script)

# Create __init__.py to mark it as a package
with open(init_file, "w", encoding="utf-8") as f:
    f.write("# API package initialization")

print(f"FastAPI project setup complete. Files created in: {base_dir}")
