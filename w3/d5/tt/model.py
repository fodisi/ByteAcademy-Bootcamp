#!/usr/bin/env python3

import json
import sqlite3

import requests

import mapper
import wrapper


def buy(ticker_symbol, trade_volume):
	# TODO replace the following value, for user_balance, with a read operation from
	# the database, which should eventualy be in our mapper.
	#user_balance = 1000.00
	connection = sqlite3.connect('master.db', check_same_thread=False)
	cursor = connection.cursor()
	#TODO write db function to get the balance
	#replace the hardcoded value with something that can handle an arbitrary username
	cursor.execute('select balance from users where username = "francis"')
	user_balance = cursor.fetcha_all()[0][0]
	print('User balance:', user_balance)
	brokerage_fee = 6.95
	last_price = get_last_price(ticker_symbol)
	transaction_cost = (last_price * float(trade_volume)) + brokerage_fee
	if transaction_cost < user_balance:
		#the user has enough money to buy
		# TODO check if symbol already exists in DB. if true, update, otherwise 

		cursor.execute('select ticker_symbol from holdings where ticker_symbol = "{0}"'.format(ticker_symbol))
		ticker_symbols = cursor.fetch_all()[0]
		if len(ticker_symbols) == 0:
			cursor.execute(
			"""
			insert into holdings 
			(
				ticker_symbol, 
				number_of_shares, 
				volume_average_weighted_price
			)
			values
			(
			{0},
			{1},
			{2}
			);""".format(
				ticker_symbol,
				trade_volume,
				last_price
			))
		else:
			#TODO update the db with a new 
			#volume_average_weighted_price and number_of_shares
			pass
		connection.commit()
		cursor.close()
		connection.close()
	else:
		return 'Error: You do not have enough money to trade what you want to.'


def sell():
	pass



def get_last_price(ticker_symbol):
	endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='+ticker_symbol
	response = json.loads(requests.get(endpoint).text)
	last_price = response['LastPrice']
	return last_price


def get_ticker_symbol(company_name):
	endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+company_name
	#TODO Re-factor following code so it doesn't just arbitrabily take the first thing in the iterable that's returned and assume it's the security we want
	response = json.loads(requests.get(endpoint).text)[0]
	ticker_symbol = response['Symbol']
	return ticker_symbol


if __name__ == '__main__':
	# Test:
	# - Buy one share of AT&T at fair price (last_price)
	print(buy('t', 1))
