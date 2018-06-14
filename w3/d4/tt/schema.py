#!usr/bin/env python3

import sqlite3


connection = sqlite3.connect('getrichquickschem.db', check_same_thread=False)
cursor = connection.cursor()

# users
cursor.execute(
	"""create table users(
		pk integer primary key autoincrement,
		username varchar(16),
		password varchar(32)
		balance float
	);"""
)


cursor.execute(
	"""create table holdings(
		pk integer primary key autoincrement,
		ticker_symbol varchar(8) UNIQUE,
		number_of_shares integer,
		volume_weighted_average_price float

	);"""
)

cursor.execute(
	"""create table orders(
		pk integer primary_key autoincrement,
		unix_time float,
		transaction_type book,
		last_price float,
		trade_volume integer
	);"""
)

connection.commit()
cursor.close()
connection.close
