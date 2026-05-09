# Memory handled by LangChain

class Memory:
    def __init__(self):
        self.history = []
        self.last_analysis = None

    def add_message(self, role, message):
        self.history.append({
            "role": role,
            "message": message
        })

    def get_history(self):
        return self.history

    def get_recent_context(self, limit=4):
        recent = self.history[-limit:]

        return " ".join([
            item["message"] for item in recent
        ])