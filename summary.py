import os
from groq import Groq
from telegram import Update

class Summary:
    def __init__(self):
        GROQ_KEY = "YOUR-GROQ-KEY"
        self.client = Groq(api_key=GROQ_KEY)

    def fetch_summary(self, query):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Me explique um pouco sobre {query}",
                }
            ],
            model="llama3-8b-8192"
        )

        return response.choices[0].message.content