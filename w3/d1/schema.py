#!/usr/bin/env python3

def create_table(ticker_symbol):
	connection = sqlite3.connect('master.db', check_same_thread=False)
	cursor = connection.cursor()
	cursor.execute('create table {0} (pk integer primary key autoincrement, last_price float)'.format(ticker_symbol)
	cursor.execute()
	connection.close()
	return True

if __name__ == '__main__':
	create_table('nke')
