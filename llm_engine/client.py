import os
from groq import Groq


class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = self._get_supported_model()

    def _get_supported_model(self) -> str:
        models = self.client.models.list().data

        for m in models:
            if "versatile" in m.id.lower():
                return m.id

        return models[0].id

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content


def get_llm_client():
    return GroqClient()
