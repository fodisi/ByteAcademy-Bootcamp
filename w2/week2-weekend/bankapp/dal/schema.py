#!/usr/bin/env python3

import sqlite3

# create a connection to the database
connection = sqlite3.connect("bankapp.db", check_same_thread=False)

# create a cursor object to represent the "gaze" of the database management system
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE banks(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR
	);"""
)

cursor.execute(
	"""CREATE TABLE branches(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		bank_id INTEGER
		name VARCHAR,
		FOREIGN KEY(bank_id) REFERENCES banks(id)
	);"""
)



cursor.close()
connection.close()
