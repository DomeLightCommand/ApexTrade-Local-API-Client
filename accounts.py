# Simple in-memory storage for testing. 
# Real implementation would use SQLite or Postgres.

_accounts = [
    {"id": "acc_1", "name": "Binance Main", "balance": 1500.0},
    {"id": "acc_2", "name": "Bybit Sub", "balance": 800.0}
]

def get_all_accounts():
    return _accounts

def update_balance(account_id: str, amount: float):
    for acc in _accounts:
        if acc["id"] == account_id:
            acc["balance"] += amount
            return True
    return False