#!/usr/bin/env python3

from bankapp.model import Bank

"""Represents an instance of a Bank"""
class BankDAL():
	def __init__(self, bank=None):
		self.__bank = Bank(5, 'francis')
	
	def print_model(self):
		print(self.__bank.name)
		print(self.__bank.id)
