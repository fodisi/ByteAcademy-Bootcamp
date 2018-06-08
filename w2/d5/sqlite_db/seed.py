#!/usr/bin/env python3

import sqlite3
import csv

# create a connection to the database
connection = sqlite3.connect("securities_master.db", check_same_thread=False)

# create a cursor object to represent the "gaze" of the database management system
cursor = connection.cursor()

with open('rippleUSD.csv') as f:
	rows = csv.reader(f)
	for row in rows:
		cursor.execute(
			"""INSERT INTO rippleUSD(
			unix_time,
			last_price,
			trade_volume
			) VALUES (
			{unix_time},
			{last_price},
			{trade_volume}
			);""".format(
				unix_time=row[0],
				last_price=row[1],
				trade_volume=row[2]
				)
			)

#This is basically saving the changes to a document
connection.commit()
cursor.close()
connection.close()
