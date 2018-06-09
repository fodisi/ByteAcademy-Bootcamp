#!/usr/bin/env python3


from person import Person


"""Represents a bank Client"""
class Client(Person):
	def __init__(self, id_=0, name=''):
		super.__init__(id_, name, 'C')
		self.accounts = {}
