#!/usr/bin/env python3

"""Represents a bank transaction, such as deposit, withdrawal, etc."""
class Transaction():
	def __init__(self, id_, date, description, amount, tx_type):
		self.id = id_
		self.date = date
		self.description = description
		self.amount = amount
		self.type = tx_type
