#!/usr/bin/env python3


"""Represents an instance of a Bank"""
class Bank():
	def __init__(self, id=0, name="", branches={}):
		self.id = id
		self.name = name
		self.branches = branches
