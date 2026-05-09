from .base_agent import BaseAgent
from .spend_analysis_agent import SpendAnalysisAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Planner Agent")
        self.spend_agent = SpendAnalysisAgent()

    def process(self, query, context=None):
        """Process query and decide which agent to invoke."""
        query_lower = query.lower()
        spending_keywords = ["spend", "analysis", "anomal", "trend", "category", "breakdown", "expense", 
                            "budget", "cost", "transaction", "money", "amount", "total", "dining", 
                            "grocery", "shopping", "entertainment", "utilities", "transportation", 
                            "healthcare", "unusual", "explain"]
        
        if any(keyword in query_lower for keyword in spending_keywords):
            result = self.spend_agent.process(query)
            response = f"Based on your query, here's the analysis:\n{result}"
        else:
            response = "I can help with spending analysis. Please ask about your spending patterns, anomalies, trends, or any expense-related questions."
        return response