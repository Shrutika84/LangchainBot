from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import FAQBot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot = FAQBot()
    response = bot.get_response(user_input)
    return jsonify({"response": response})
    
@app.route("/", methods=["GET"])
def home():
    return "LangChain Bot is running! Use the /chat endpoint."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  
    app.run(host="0.0.0.0", port=port, debug=False)
