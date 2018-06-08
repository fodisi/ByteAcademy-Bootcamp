#!/usr/bin/env python3

import json
import requests


def get_price(ticker_symbol):
	endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=' + ticker_symbol
	response = json.loads(requests.get(endpoint).text)['LastPrice']
	return response


def get_symbol(company_name):
	endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input=' + company_name
	response = json.loads(requests.get(endpoint).text)[0]['Symbol']
	return response


if __name__ == '__main__':
	print(get_price('tsla'))
	print(get_symbol('tesla'))
	print(get_price(get_symbol('tesla')))

