import streamlit as st
from datetime import datetime

class Transaction:
    def __init__(self, amount, type, timestamp=None):
        self.amount = amount
        self.type = type
        self.timestamp = timestamp or datetime.now()


    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.type}: ₦{self.amount}"



