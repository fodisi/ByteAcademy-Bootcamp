#!/usr/bin/env python3

import sqlite3

# create a connection to the database
connection = sqlite3.connect("bankapp.db", check_same_thread=False)

# create a cursor object to represent the "gaze" of the database management system
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE banks(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(100)
	);"""
)

cursor.execute(
	"""CREATE TABLE branches(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		bank_id INTEGER,
		name VARCHAR(100),
		FOREIGN KEY(bank_id) REFERENCES banks(id)
	);"""
)

cursor.execute(
	"""CREATE TABLE accounts(
		number INTEGER PRIMARY KEY AUTOINCREMENT,
		branch_id INTEGER,
		FOREIGN KEY(branch_id) REFERENCES branches(id)
	);"""
)

cursor.execute(
	"""CREATE TABLE transactions(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		account_number INTEGER,
		date DATETIME,
		type VARCHAR(1),
		description VARCHAR(100),
		amount float,
		FOREIGN KEY(account_number) REFERENCES accounts(number)
	);"""
)

cursor.execute(
	"""CREATE TABLE people(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(150),
		email VARCHAR(100),
		role VARCHAR(1),
		login VARCHAR(15) UNIQUE,
		password VARCHAR(25)
	);"""
)

cursor.execute(
	"""CREATE TABLE client_accounts(
		client_id INTEGER,
		account_number INTEGER UNIQUE,
		PRIMARY KEY (client_id, account_number)
		FOREIGN KEY(client_id) REFERENCES people(id),
		FOREIGN KEY(account_number) REFERENCES accounts(number)
	);"""
)



cursor.close()
connection.close()
