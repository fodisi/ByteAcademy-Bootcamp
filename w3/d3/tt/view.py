#!/usr/bin/env python3

import os

def main_menu():
	os.system('clear')
	print('\nWelcome to westworld!\n')
	user_input = input('What do you want to do?')
	return user_input


def quote_menu():
	os.system('clear')
	print('\nTerminal trader\n')
	ticker_symbol = input('Ticker symbol:')
	return ticker_symbol
