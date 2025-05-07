from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import pandas as pd
import requests
import re
from fuzzywuzzy import process
import os

class FAQBot:
    def __init__(self, faq_file="FAQ_updated.csv"):
        print("🔄 Loading CSV data...")
        self.faq_file = faq_file
        self.faq_data = self.load_faq_data()

        # ✅ FREE LLM via HuggingFace (no OpenAI key needed)
        self.llm = HuggingFaceHub(
            repo_id="google/flan-t5-small",
            model_kwargs={"temperature": 0.5, "max_length": 100}
        )

        self.prompt = PromptTemplate(
            input_variables=["question"],
            template="""
            You're an assistant for a nonprofit. Be clear and helpful.
            Question: {question}
            Answer:
            """
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

        self.basic_questions = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hi there! How can I help?",
            "hey": "Hey! How can I support you?",
            "how are you": "I'm just a chatbot, but I'm here to help! How can I assist you?",
            "who are you": "I'm the House of Good Deeds AI chatbot! I can help you with event details, donations, and volunteer information.",
            "what do you do": "I assist with answering FAQs, providing donation details, and updating you on upcoming events!",
            "how can you help me": "I can provide information on volunteering, donations, and upcoming events. Just ask!",
        }

    def load_faq_data(self):
        try:
            abs_path = os.path.abspath(self.faq_file)
            print(f"📍 Loading CSV from: {abs_path}")
            faq_data = pd.read_csv(abs_path, encoding="latin1")
            return faq_data
        except Exception as e:
            print("❌ Error loading FAQ data:", e)
            return pd.DataFrame(columns=["Question", "Answer"])

    def get_best_match(self, user_input, faq_data):
        all_variants = []
        mapping = {}

        for _, row in faq_data.iterrows():
            variants = str(row["Question"]).split(" | ")
            for variant in variants:
                all_variants.append(variant.lower())
                mapping[variant.lower()] = row["Answer"]

        matches = process.extract(user_input.lower(), all_variants, limit=5)
        best_match, score = matches[0]
        print(f"[DEBUG] Best Match: {best_match} | Score: {score}")

        return mapping.get(best_match) if score > 75 else None

    def get_llm_response(self, prompt_text):
        return self.chain.run(prompt_text)

    def get_response(self, user_input):
        faq_data = self.load_faq_data()
        user_input_lower = user_input.lower().strip()

        # Hardcoded responses
        for pattern, response in self.basic_questions.items():
            if re.search(rf"\b{pattern}\b", user_input_lower):
                return response

        # CSV lookup
        if not faq_data.empty:
            matched_answer = self.get_best_match(user_input, faq_data)
            if matched_answer:
                return matched_answer

        # Custom image triggers
        if "volunteer photos" in user_input_lower:
            return """Here are some moments from our past events:<br>
            <img src='photos/take2.jpg' width='200'/>
            """

        # FLAN fallback
        print("🤖 Falling back to FLAN-T5")
        return self.get_llm_response(f"Answer this community question: {user_input}")
