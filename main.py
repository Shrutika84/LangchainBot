from flask import Flask, request, jsonify, render_template
import os
from chatbot import FAQBot
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route("/")
def home():
    return render_template("new_chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot = FAQBot()
    response = bot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
