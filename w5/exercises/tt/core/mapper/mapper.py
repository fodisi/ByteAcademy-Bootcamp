#!/usr/bin/env python3

import sqlite3 as db
from datetime import datetime


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


""" Functions for manipulating data from Users table. """


def select_user(username):
    sql_cmd = """
        SELECT 
            pk,
            username,
            password,
            profile,
            initial_balance,
            cur_balance
        FROM
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
        user['profile'] = row[3]
        user['initial_balance'] = row[4]
        user['cur_balance'] = row[5]
        return user
    else:
        return None


def select_all_users():
    sql_cmd = """
        SELECT
            pk,
            username,
            password,
            profile,
            initial_balance,
            cur_balance
        FROM
            users
        ;"""

    result = __execute_query(sql_cmd)

    if len(result) > 0:
        user_list = []
        for row in result:
            user = {}
            user['pk'] = row[0]
            user['username'] = row[1]
            user['password'] = row[2]
            user['profile'] = row[3]
            user['initial_balance'] = row[4]
            user['cur_balance'] = row[5]
            user_list.append(user)
        return user_list
    else:
        return None


def select_current_balance(username):
    sql_cmd = """
        SELECT
            cur_balance
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


def select_balance_for_pl(username):
    sql_cmd = """
        SELECT
            initial_balance,
            cur_balance
        FROM
            users
        WHERE
            username = '{username}'
        ; """.format(username=username)

    result = __execute_query(sql_cmd)

    if len(result) > 0:
        row = result[0]
        # Returns: initial balance | current balance
        return row[0], row[1]
    else:
        return 0, 0


def update_balance(username, balance):
    sql_cmd = """
        UPDATE
            users
        SET
            cur_balance = {balance}
        WHERE
            username = '{username}'
        ; """.format(
        username=username,
        balance=balance
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
            profile,
            initial_balance,
            cur_balance
        )
        VALUES
        (
            '{username}',
            '{password}',
            'U',
            100000,
            100000

        )
        ; """.format(
        username=username,
        password=password
    )
    __execute_non_query(sql_cmd)
    return True


def delete_user(username):
    # TODO Make all SQL commands execute in the same DB transaction.

    user = select_user(username)
    if user == None:
        return False

    if user['profile'] == 'A':
        return False

    # Deletes all user orders
    sql_cmd = "DELETE FROM orders WHERE username='{0}'".format(username)
    __execute_non_query(sql_cmd)

    # Deletes all holdings
    sql_cmd = "DELETE FROM holdings WHERE username='{0}'".format(username)
    __execute_non_query(sql_cmd)

    # Deletes user
    sql_cmd = "DELETE FROM users WHERE username='{0}'".format(username)
    __execute_non_query(sql_cmd)

    return True


""" Functions for manipulating data from Holdings table. """


def select_holdings_by_symbol(username, ticker_symbol):
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
        holding = {}
        row = result[0]
        holding['pk'] = row[0]
        holding['username'] = row[1]
        holding['ticker_symbol'] = row[2]
        holding['volume'] = row[3]
        holding['average_price'] = row[4]
        return holding
    else:
        return None


def select_holdings_by_username(username):
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
            volume > 0
        ORDER BY
            volume DESC
        ; """.format(username=username)

    result = __execute_query(sql_cmd)

    if len(result) > 0:
        holding_list = []
        for row in result:
            holding = {}
            holding['pk'] = row[0]
            holding['username'] = row[1]
            holding['ticker_symbol'] = row[2]
            holding['volume'] = row[3]
            holding['average_price'] = row[4]
            holding_list.append(holding)
        return holding_list
    else:
        return None


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


def update_holdings(username, ticker_symbol, volume, average_price):
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


""" Functions for manipulating data from Orders table. """


def insert_order(username,
                 ticker_symbol,
                 date_time,
                 transaction_type,
                 unit_price,
                 volume,
                 fee):
    sql_cmd = """
        INSERT INTO
            orders
        (
            username,
            ticker_symbol,
            date_time,
            transaction_type,
            unit_price,
            volume,
            fee
        )
        VALUES
        (
            '{username}',
            '{ticker_symbol}',
            '{date_time}',
            '{transaction_type}',
            {unit_price},
            {volume},
            {fee}

        )
        ; """.format(
        username=username,
        ticker_symbol=ticker_symbol,
        date_time=date_time,
        transaction_type=transaction_type,
        unit_price=unit_price,
        volume=volume,
        fee=fee
    )
    __execute_non_query(sql_cmd)
    return True


def select_order_history(username):
    sql_cmd = """
        SELECT
            pk,
            username,
            ticker_symbol,
            strftime('%Y/%m/%d %H:%M:%S', date_time),
            transaction_type,
            unit_price,
            volume,
            fee
        FROM
            orders
        WHERE
            username = '{username}'
        ORDER BY
            date_time
        ; """.format(
        username=username)

    result = __execute_query(sql_cmd)

    if len(result) > 0:
        order_list = []
        for row in result:
            order = {}
            order['pk'] = row[0]
            order['username'] = row[1]
            order['ticker_symbol'] = row[2]
            order['date_time'] = datetime.strptime(row[3],
                                                   '%Y/%m/%d  %H:%M:%S')
            order['order_type'] = row[4]
            order['unit_price'] = row[5]
            order['volume'] = row[6]
            order['fee'] = row[7]
            order_list.append(order)
        return order_list
    else:
        return None
