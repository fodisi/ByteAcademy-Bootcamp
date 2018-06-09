#!/usr/bin/env python3


"""Representation of a bank Branch"""
class Branch():
	def __init__(self, id_=0, name=""):
		self.id = id_
		self.name = name
		self.accounts = {}


	def create_account(self, account)
		self.accounts[account.number] = account
