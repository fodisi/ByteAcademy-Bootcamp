#!/usr/bin/env python3
import psycopg2
from psycopg2.extras import RealDictCursor


connection = psycopg2.connect('dbname=btc_prices')
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor(cursor_factory=RealDictCursor)

cursor.execute(
	""" create table krakenUSD(
		pk serial primary key,
		unix_time integer,
		last_price float,
		trade_volume float
	);"""
)

cursor.close()
connection.close()

print('done')
