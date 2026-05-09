from .base_agent import BaseAgent
from .spend_analysis_agent import SpendAnalysisAgent
from ..memory.memory import Memory
from ..llm.local_llm import LocalLLM

class PlannerAgent(BaseAgent):
    def __init__(self, memory = None):
        super().__init__("Planner Agent")
        self.memory = memory
        self.llm = LocalLLM()
        self.spend_agent = SpendAnalysisAgent()

    def process(self, query, context=None):
        """Process query and decide which agent to invoke."""
        #query_lower = query.lower()
        previous_context = ""

        if self.memory:
            previous_context = self.memory.get_recent_context()

        combined_query = f"{previous_context} {query}"

        query_lower = combined_query.lower()
        spending_keywords = ["spend", "analysis", "anomal", "trend", "category", "breakdown", "expense", 
                            "budget", "cost", "transaction", "money", "amount", "total", "dining", 
                            "grocery", "shopping", "entertainment", "utilities", "transportation", 
                            "healthcare", "unusual", "explain", "finance", "finances", "anomaly",
                            "anomalies", "above", "previous",]
        
        if any(keyword in query_lower for keyword in spending_keywords):
            result = self.spend_agent.process(query)
            if self.memory:
                self.memory.last_analysis_data = self.spend_agent.analysis_data
            #response = f"Based on your query, here's the analysis:\n{result}"
            prompt = f"""
            You are a personal finance advisor.

            User question:
            {query}

            Financial analysis data:
            {result}

            Rules:
            - Answer conversationally
            - No tables
            - No markdown
            - Be concise and helpful
            """

            response = self.llm.generate(prompt)
            if self.memory:
                self.memory.last_analysis = result
        else:
            response = "I can help with spending analysis. Please ask about your spending patterns, anomalies, trends, or any expense-related questions."
        return response