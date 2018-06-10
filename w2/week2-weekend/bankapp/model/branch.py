#!/usr/bin/env python3


"""Represents a bank Branch"""
class Branch():
	def __init__(self, id_=0, name="", bank_id=0):
		self.id = id_
		self.bank_id = bank_id
		self.name = name
		self.accounts = {}


	def create_account(self, account):
		account.branch_id = self.id
		self.accounts[account.number] = account


	def account_exists(self, number):
		return number in self.accounts
