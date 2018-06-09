#!/usr/bin/env python3


"""Represents an instance of a bank Branch"""
class Branch():
	def __init__(self, id=0, name=""):
		self.id = id
		self.name = name
		self.accounts = {}
