#!/usr/bin/env python3


from model.transaction import Transaction
from model.client import Client


"""Represents a bank Account"""
class Account():
	def __init__(self, number=0, branch_id=0, client = None):
		self.number = number
		self.branch_id = branch_id
		self.client = client
		self.__transactions = []


	def deposit(self, tx_id, date, description, amount):
		tx = Transaction(tx_id, date, description, amount, 'D', self.number)
		self.__transactions.append(tx)
		

	def withdrawal(self, tx_id, date, description, amount):
		tx = Transaction(tx_id, date, description, amount * -1, 'W', self.number)
		self.__transactions.append(tx)
	

	def get_balance(self):
		return sum(tx.amount for tx in self.__transactions)


	def get_transaction_history(self):
		history = self.__transactions[::]
		history.sort(key=lambda x: x.date)
		return history
			
