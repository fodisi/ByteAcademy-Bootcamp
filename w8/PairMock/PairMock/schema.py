#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect('master.db',check_same_thread=False)
cursor     = connection.cursor()

cursor.execute(
    """CREATE TABLE products(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        price FLOAT,
        path_name VARCHAR(32)
    );"""
)

cursor.close()
connection.close()