from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import FAQBot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot = FAQBot()
    response = bot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
