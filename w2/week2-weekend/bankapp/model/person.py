#!/usr/bin/env python3

"""Represents a Person"""
class Person():
	def __init__(self, id_=0, name='', email='', role=''):
		self.id = id_
		self.name = name
		self.email = email
		self.__role = role
		self.login = ''
		self.password = ''
