#!/usr/bin/env python3

import sqlite3 as db


def __execute_non_query(sql_command):
    # creates a connection to the database
    with db.connect('master.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        """SQLite3 requires that this command be executed to active
        Foreign Key constrains
        Link: https://www.sqlite.org/foreignkeys.html#fk_enable"""
        cursor.execute("PRAGMA foreign_keys = ON;")
        # executes and commits the sql command
        cursor.execute(sql_command)
        conn.commit()
        cursor.close()


def __execute_query(sql_command):
    # creates a connection to the database
    with db.connect('master.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        # executes sql command and returns fetched data
        cursor.execute(sql_command)
        return cursor.fetchall()


def select_user(username):
    sql_cmd = """
        SELECT * FROM
            users
        WHERE
            username = '{username}'
        ; """.format(
        username=username
    )
    result = __execute_query(sql_cmd)

    if len(result) > 0:
        user = {}
        row = result[0]
        user['pk'] = row[0]
        user['username'] = row[1]
        user['password'] = row[2]
        user['balance'] = row[3]
        return user
    else:
        return None


def select_user_balance(username):
    sql_cmd = """
        SELECT
            balance
        FROM
            users
        WHERE
            username = '{username}'
        ; """.format(
        username=username
    )
    result = __execute_query(sql_cmd)

    if len(result) > 0:
        row = result[0]
        return row[0]
    else:
        return 0


def select_user_holdings_by_symbol(username, ticker_symbol):
    sql_cmd = """
        SELECT
            pk,
            username,
            ticker_symbol,
            volume,
            average_price
        FROM
            holdings
        WHERE
            username = '{username}'
        AND
            ticker_symbol = '{ticker_symbol}'
        ; """.format(
        username=username,
        ticker_symbol=ticker_symbol
    )
    result = __execute_query(sql_cmd)

    if len(result) > 0:
        holdings = {}
        row = result[0]
        holdings['pk'] = row[0]
        holdings['username'] = row[1]
        holdings['ticker_symbol'] = row[2]
        holdings['volume'] = row[3]
        holdings['average_price'] = row[4]
        return holdings
    else:
        return None


def insert_order(username,
                 ticker_symbol,
                 date_time,
                 transaction_type,
                 unit_price,
                 volume):
    sql_cmd = """
        INSERT INTO
            orders
        (
            username,
            ticker_symbol,
            date_time,
            transaction_type,
            unit_price,
            volume
        )
        VALUES
        (
            '{username}',
            '{ticker_symbol}',
            '{date_time}',
            '{transaction_type}',
            {unit_price},
            {volume}

        )
        ; """.format(
        username=username,
        ticker_symbol=ticker_symbol,
        date_time=date_time,
        transaction_type=transaction_type,
        unit_price=unit_price,
        volume=volume
    )
    __execute_non_query(sql_cmd)
    return True


def insert_holdings(username, ticker_symbol, volume, average_price):
    sql_cmd = """
        INSERT INTO
            holdings
        (
            username,
            ticker_symbol,
            volume,
            average_price
        )
        VALUES
        (
            '{username}',
            '{ticker_symbol}',
            {volume},
            {average_price}
        )
        ; """.format(
        username=username,
        ticker_symbol=ticker_symbol,
        volume=volume,
        average_price=average_price
    )
    __execute_non_query(sql_cmd)
    return True


def insert_user(username, password):
    sql_cmd = """
        INSERT INTO
            users
        (
            username,
            password,
            balance
        )
        VALUES
        (
            '{username}',
            '{password}',
            100000

        )
        ; """.format(
        username=username,
        password=password
    )
    __execute_non_query(sql_cmd)
    return True


def update_user_holdings(username, ticker_symbol, volume, average_price):
    sql_cmd = """
        UPDATE
            holdings
        SET
            volume = {volume},
            average_price = {average_price}
        WHERE
            username = '{username}'
        AND
            ticker_symbol = '{ticker_symbol}'
        ; """.format(
        username=username,
        ticker_symbol=ticker_symbol,
        volume=volume,
        average_price=average_price
    )
    __execute_non_query(sql_cmd)
    return True


def update_user_balance(username, balance):
    sql_cmd = """
        UPDATE
            users
        SET
            balance = {balance}
        WHERE
            username = '{username}'
        ; """.format(
        username=username,
        balance=balance
    )
    __execute_non_query(sql_cmd)
    return True
