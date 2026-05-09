import random
from datetime import datetime, timedelta

# Mock transaction data
def mock_fetch_transactions(user_id, months=3, target_month=None):
    """Mock function to fetch transaction data for a user.
    
    Args:
        user_id: User identifier
        months: Number of months to generate data for (if target_month not specified)
        target_month: Specific month to fetch (format: "2026-05" or "May 2026")
    """
    categories = ["Groceries", "Dining", "Entertainment", "Utilities", "Transportation", "Shopping", "Healthcare"]
    transactions = []
    base_date = datetime.now()
    
    if target_month:
        # Generate data specifically for the target month
        # Parse target_month format
        if len(target_month.split('-')) == 2:
            year, month = target_month.split('-')
            year, month = int(year), int(month)
        else:
            # Try to parse "May 2026" format
            import calendar
            parts = target_month.split()
            month_name = parts[0]
            year = int(parts[1]) if len(parts) > 1 else base_date.year
            month = list(calendar.month_name).index(month_name)
        
        # Generate transactions for the target month
        target_date = datetime(year, month, 1)
        days_in_month = 30 if month != 2 else 28
        for day in range(1, days_in_month + 1):
            date = datetime(year, month, day)
            # Generate 1-3 transactions per day
            for _ in range(random.randint(1, 3)):
                amount = round(random.uniform(10, 300), 2)
                category = random.choice(categories)
                description = f"{category} Transaction"
                transactions.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "amount": amount,
                    "category": category,
                    "description": description
                })
    else:
        # Generate data for last N months (default behavior)
        for i in range(months * 30):  # Approx 30 days per month
            date = base_date - timedelta(days=i)
            amount = round(random.uniform(10, 500), 2)
            category = random.choice(categories)
            description = f"Transaction {i+1}"
            transactions.append({
                "date": date.strftime("%Y-%m-%d"),
                "amount": amount,
                "category": category,
                "description": description
            })
    
    return transactions

# Mock categorization (already categorized in mock data)
def mock_categorize_expenses(transactions):
    """Categorize expenses (mock, as data is already categorized)."""
    return transactions

# Mock trend calculation
def mock_calculate_trends(transactions):
    """Calculate monthly spending trends."""
    monthly_totals = {}
    for tx in transactions:
        month = tx["date"][:7]  # YYYY-MM
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += tx["amount"]
    return monthly_totals

# Mock anomaly detection
def mock_detect_anomalies(transactions, threshold=1000):
    """Detect unusual spending patterns (e.g., if monthly total > threshold)."""
    trends = mock_calculate_trends(transactions)
    anomalies = []
    for month, total in trends.items():
        if total > threshold:
            anomalies.append(f"Unusual spending in {month}: ${total:.2f}")
    return anomalies