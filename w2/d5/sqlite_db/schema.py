#!/usr/bin/env python3

import sqlite3

# create a connection to the database
connection = sqlite3.connect("securities_master.db", check_same_thread=False)

# create a cursor object to represent the "gaze" of the database management system
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE rippleUSD(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		unix_time FLOAT,
		last_price FLOAT,
		trade_volume FLOAT
	);"""
)

cursor.close()
connection.close()
