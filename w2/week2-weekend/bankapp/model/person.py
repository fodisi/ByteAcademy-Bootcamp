#!/usr/bin/env python3

"""Representation a Person"""
class Person():
	def __init__(self, id_=0, name='', email='', person_type=''):
		self.id = id_
		self.name = name
		self.email = email
		self.type = person_type
		self.login = ''
		self.password = ''
