#!/usr/bin/env python3

"""Representation of a bank Account"""
class Account():
	def __init__(self, number=0, client = None):
		self.number = number
		self.client = client

	def deposit(self, tx_id, date, description, amout):
		pass

	def withdrawal(self, tx_id, date, description, amout):
		pass
	
	def get_balance(self):
		pass
