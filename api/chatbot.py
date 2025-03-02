from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(port=5000)
