import requests

class LocalLLM:
    def __init__(self, model="llama3"):
        self.model = model

    def generate(self, prompt: str):
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        return res.json()["response"]