#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect('master.db',check_same_thread=False)
cursor     = connection.cursor()

cursor.execute(
    """INSERT INTO products(
        name,
        price,
        path_name) VALUES(
        'abaci',
        100,
        'abaci.jpg'
        );"""
)

cursor.execute(
    """INSERT INTO products(
        name,
        price,
        path_name) VALUES(
        'aback',
        110,
        'aback.jpg'
        );"""
)

cursor.execute(
    """INSERT INTO products(
        name,
        price,
        path_name) VALUES(
        'abacus',
        120,
        'abacus.jpg'
        );"""
)

cursor.execute(
    """INSERT INTO products(
        name,
        price,
        path_name) VALUES(
        'return',
        155,
        'url_for.jpg'
        );"""
)

connection.commit()
cursor.close()
connection.close()