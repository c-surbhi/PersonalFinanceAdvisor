import re
from .base_agent import BaseAgent
from ..tools.mock_tools import mock_fetch_transactions, mock_categorize_expenses, mock_calculate_trends, mock_detect_anomalies

class SpendAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Spend Analysis Agent")

    def extract_month_from_query(self, query):
        """Extract month information from user query."""
        query_lower = query.lower()
        
        # Try to find patterns like "may 2026", "05/2026", "2026-05"
        month_names = ["january", "february", "march", "april", "may", "june", 
                      "july", "august", "september", "october", "november", "december"]
        
        for month_name in month_names:
            if month_name in query_lower:
                # Look for year after month name
                year_match = re.search(r'\b(20\d{2})\b', query)
                if year_match:
                    year = year_match.group(1)
                    return f"{month_name.capitalize()} {year}"
                else:
                    from datetime import datetime
                    return f"{month_name.capitalize()} {datetime.now().year}"
        
        return None

    def process(self, query):
        """Analyze spending based on query."""
        user_id = "user123"
        
        # Extract month if specified in query
        target_month = self.extract_month_from_query(query)
        
        if target_month:
            transactions = mock_fetch_transactions(user_id, target_month=target_month)
            month_label = target_month
        else:
            transactions = mock_fetch_transactions(user_id)
            month_label = "last 3 months"
        categorized = mock_categorize_expenses(transactions)
        trends = mock_calculate_trends(categorized)
        anomalies = mock_detect_anomalies(categorized)

        total_spent = sum(tx["amount"] for tx in transactions)
        category_totals = {}
        for tx in categorized:
            cat = tx["category"]
            category_totals[cat] = category_totals.get(cat, 0) + tx["amount"]

        insights = f"## Spending Analysis for {month_label}\n"
        insights += f"**Total Spent: ${total_spent:.2f}**\n\n"
        
        if category_totals:
            insights += "### Category Breakdown\n"
            insights += "| Category | Amount | Percentage |\n"
            insights += "|----------|--------|------------|\n"
            for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
                pct = (amt / total_spent * 100) if total_spent > 0 else 0
                insights += f"| {cat} | ${amt:.2f} | {pct:.1f}% |\n"
        
        if trends:
            insights += "\n### Monthly Trends\n"
            insights += "| Month | Total Spent |\n"
            insights += "|-------|-------------|\n"
            for month, amt in sorted(trends.items()):
                insights += f"| {month} | ${amt:.2f} |\n"
        
        if anomalies:
            insights += "\n### ⚠️ Anomalies Detected\n"
            insights += "\n".join(anomalies)
        else:
            insights += "\n### ✅ No unusual spending detected."

        return insights