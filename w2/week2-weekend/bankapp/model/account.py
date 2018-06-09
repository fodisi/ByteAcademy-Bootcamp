#!/usr/bin/env python3


from transaction import Transaction
from client import Client


"""Represents a bank Account"""
class Account():
	def __init__(self, number=0, client = None):
		self.number = number
		self.client = client
		self.__transactions = []


	def deposit(self, tx_id, date, description, amount):
		tx = Transaction(tx_id, date, description, amount, 'D')
		self.__transactions.append(tx)
		

	def withdrawal(self, tx_id, date, description, amount):
		tx = Transaction(tx_id, date, description, amount * -1, 'W')
		self.__transactions.append(tx)
	

	def get_balance(self):
		return sum(tx.amount for tx in self.__transactions)
