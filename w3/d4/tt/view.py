#!/usr/bin/env python3

import os

def display_header():
	os.system('clear')
	print('*************************')
	print('**                     **')
	print('*    Terminal Trader    *')
	print('**                     **')
	print('*************************')


def main_menu():
	display_header()
	user_input = input('What do you want to do?')
	return user_input


def lookup_menu():
	display_header()
	poop = input('Company Name: ')
	return poop


def quote_menu():
	display_header()
	ticker_symbol = input('Ticker symbol:')
	return ticker_symbol
