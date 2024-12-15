import os
from groq import Groq
from telegram import Update

class Summary:
    def __init__(self):
        self.client = "YOUR-GROQ-API-KEY-HERE"

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