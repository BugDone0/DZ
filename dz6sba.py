from datetime import datetime
from decimal import Decimal
from collections import deque

class Account:
    def __init__(self, name: str, initial_balance: float = 0.0):
        self.name = name
        self.balance = Decimal(str(initial_balance))
        self.history = deque()

    def deposit(self, amount: float):
        amount_decimal = Decimal(str(amount))
        self.balance += amount_decimal
        self.history.append({
            "type": "deposit",
            "amount": amount_decimal,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def withdraw(self, amount: float):
        amount_decimal = Decimal(str(amount))
        if amount_decimal > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount_decimal
        self.history.append({
            "type": "withdraw",
            "amount": amount_decimal,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_balance(self):
        return self.balance

    def get_history(self):
        return list(self.history)

# Пример использования
account = Account("Amogus Ivanov", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print("User name:", account.name)
print("Balance:", account.get_balance())
print("History:", account.get_history())
