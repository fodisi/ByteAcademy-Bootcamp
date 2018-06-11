#!/usr/bin/env python3


import sqlite3 #import standard library

def record_price(ticker_symbol, last_price):
	connection = sqlite3.connect('master.db', check_same_thread=False)
	cursor = connection.cursor()
	cursor.execute('insert into {0}(last_price) values ({1});'.format(ticker_symbol, last_price))
	connection.commit()
	cursor.close()
	connection.close()
	return True

if __name__ == '__main__':
	record_price('tsla', 317.66)
