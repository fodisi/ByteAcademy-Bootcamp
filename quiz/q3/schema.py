#!usr/bin/env python3

import sqlite3


connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE historyMSFT(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		date DATETIME,
		open FLOAT,
		high FLOAT,
		low FLOAT,
		close FLOAT,
		adj_close FLOAT,
		volume FLOAT
	);"""
)


connection.commit()
cursor.close()
connection.close

