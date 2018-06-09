#!/usr/bin/env python3

"""Representation of a bank transaction, such as deposit, withdrawal, etc."""
class Transaction():
	def __init__(self, id_, date, description, amout, tx_type):
		self.id = id_
		self.date = date
		self.description = description
		self.amout = amout
		self.type = tx_type
