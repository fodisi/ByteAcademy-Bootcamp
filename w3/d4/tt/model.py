#!/usr/bin/env python3

import json

import requests

import mapper
import wrapper


def buy(ticker_symbol, trade_volume):
	# TODO replace the following value, for user_balance, with a read operation from
	# the database, which should eventualy be in our mapper.
	user_balance = 1000.00
	brokerage_fee = 6.95
	transaction_cost = (get_last_price(ticker_symbol) * float(trade_volume)) + brokerage_fee
	if last_price * float(trade_volume) < user_balance:
		return 'You don\'t have enought money, broke boy!'
	else:
		print(str(get_last_price(ticker_symbol)))
		print(str(transaction_cost))
		return 'Your trade was successful.'


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
