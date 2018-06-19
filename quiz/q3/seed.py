#!/usr/bin/env python3

from datetime import datetime
import sqlite3
import csv


connection = sqlite3.connect("master.db", check_same_thread=False)

cursor = connection.cursor()

with open('MSFT.csv') as f:
	rows = csv.reader(f)
	next(rows, None)
	for row in rows:
		sql_cmd = """INSERT INTO historyMSFT
		(
			date,
			open,
			high,
			low,
			close,
			adj_close,
			volume
		)
		VALUES
		(
			'{date}',
			{open},
			{high},
			{low},
			{close},
			{adj_close},
			{volume}
		);""".format(
				date= datetime.strptime(row[0], '%Y-%m-%d'),
				open=float(row[1]),
				high=float(row[2]),
				low=float(row[3]),
				close=float(row[4]),
				adj_close=float(row[5]),
				volume=float(row[6]),
			)
		print(sql_cmd)
		cursor.execute(sql_cmd)

connection.commit()
cursor.close()
connection.close()

