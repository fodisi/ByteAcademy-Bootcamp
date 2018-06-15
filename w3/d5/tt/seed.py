#!usr/bin/env python3

import sqlite3


connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

# users
cursor.execute(
	"""
	insert into users
	(
		username,
		password,
		balance
	)
	values
	(
		'francis',
		'123',
		100000.00
	)
	"""


connection.commit()
cursor.close()
connection.close
