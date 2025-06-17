import streamlit as st
from datetime import datetime

class Transaction:
    def __init__(self, amount, type, timestamp=None):
        self.amount = amount
        self.type = type
        self.timestamp = timestamp or datetime.now()


    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.type}: ₦{self.amount}"

class SavingsAccount:
    def __init__(self, balance=0, withdrawal_limit=5000):
        self.balance = balance
        self.withdrawal_limit = withdrawal_limit
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(amount, "Deposit")
            self.history.append(transaction)
            return f"✅ Deposited ₦{amount}"
        return "❌ Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"❌ Cannot withdraw more than ₦{self.withdrawal_limit} at once"
        elif amount > self.balance:
            return "❌ Insufficient funds"
        elif amount <= 0:
            return "❌ Invalid withdrawal amount"
        else:
            self.balance -= amount
            transaction = Transaction(amount, "Withdraw")
            self.history.append(transaction)
            return f"✅ Withdrawn ₦{amount}"

    def get_history(self):
        return self.history

class CurrentAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(amount, "Deposit")
            self.history.append(transaction)
            return f"✅ Deposited ₦{amount}"
        return "❌ Invalid deposit amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "❌ Insufficient funds"
        elif amount <= 0:
            return "❌ Invalid withdrawal amount"
        else:
            self.balance -= amount
            transaction = Transaction(amount, "Withdraw")
            self.history.append(transaction)
            return f"✅ Withdrawn ₦{amount}"

    def get_history(self):
        return self.history



