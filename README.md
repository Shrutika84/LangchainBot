# LangchainBot
# 🤖 HoGD Chatbot

A lightweight AI-powered FAQ chatbot for the nonprofit *House of Good Deeds*, built with Flask, LangChain, and a free Hugging Face model (`FLAN-T5`).

---

## 📁 Project Structure

```bash
hogd-chatbot/
├── chatbot.py              # Core logic: handles CSV FAQs, fallback to FLAN-T5
├── main.py                 # Flask app with API endpoint
├── requirements.txt        # Python dependencies
├── .env                    # Hugging Face token (optional)
├── FAQ_updated.csv         # CSV of questions and answers
├── templates/
│   └── new_chat.html       # Voice-enabled chatbot UI
```

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.8+
- Hugging Face account with a free API token: https://huggingface.co/settings/tokens

### 🔐 .env Setup
Create a `.env` file in the root:

```bash
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

> ⚠️ Or directly assign the token in `main.py` via `os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_token"`

### 🛠️ Install Dependencies
```bash
pip install -r requirements.txt
```


## 🧠 Features

- ✅ CSV-based FAQ matching using `fuzzywuzzy`
- 🔁 LLM fallback (FLAN-T5) for unseen questions
- 🖼️ Support for image responses via HTML tags
- 🎤 Voice-to-text input & text-to-speech output (browser-based)
- ⚡ Fast and 100% free LLM via Hugging Face

---

## 💡 FAQ Format (`FAQ_updated.csv`)

| Question                                   | Answer                                               |
|-------------------------------------------|-------------------------------------------------------|
| how can I donate | You can donate by dropping items or scheduling pickup |

> Support multi-intent by separating variants with ` | ` in the "Question" column

---



## 🙌 Credits
- Powered by [LangChain](https://www.langchain.com/)
- Model: [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small)

---

## 📬 Contact
Feel free to fork, reuse, or contribute!

Built for House of Good Deeds ❤️
