#!/usr/bin/env python3

import json
import sqlite3
from datetime import datetime

import requests

import mapper
import wrapper


def login(username, password):
    user = mapper.select_user(username)
    if user != None:
        return (user['username'] == username) and (user['password'] == password)
    return False


def create_user(username, password):
    return mapper.insert_user(username, password)


def get_user_balance(username):
    return mapper.select_user_balance(username)


def get_user_holdings_by_symbol(username, ticker_symbol):
    return mapper.select_user_holdings_by_symbol(username, ticker_symbol)


def get_holding_volume_by_symbol(username, ticker_symbol):
    holding_volume = 0
    holdings = get_user_holdings_by_symbol(username, ticker_symbol)
    if holdings != None:
        holding_volume = holdings['volume']
    return holding_volume


def update_user_holdings(username, ticker_symbol, trade_volume, trade_unit_price, transaction_type):
    holdings = get_user_holdings_by_symbol(username, ticker_symbol)

    if holdings != None:
        if transaction_type == 'B':
            # finds the new weighted average unit price and new volume
            total_weighted_price = holdings['volume'] * \
                holdings['average_price']
            total_weighted_price += trade_volume * trade_unit_price
            total_volume = holdings['volume'] + trade_volume
            weighted_avg_price = total_weighted_price / float(total_volume)
            mapper.update_user_holdings(username,
                                        ticker_symbol,
                                        total_volume,
                                        weighted_avg_price)
        elif transaction_type == 'S':
            # when selling, the average price of holdings doesn't change,
            # except when remaining volume is 0
            holding_volume = holdings['volume']
            holding_avg_price = holdings['average_price']
            new_volume = holding_volume - trade_volume
            if new_volume == 0:
                holding_avg_price = 0
            mapper.update_user_holdings(username,
                                        ticker_symbol,
                                        new_volume,
                                        holding_avg_price)
        else:
            raise Exception('Invalid transaction type')
    else:
        mapper.insert_holdings(username, ticker_symbol,
                               trade_volume, trade_unit_price)


def update_user_balance(username, balance):
    return mapper.update_user_balance(username, balance)


def buy(ticker_symbol, trade_volume, username):
    user_balance = get_user_balance(username)
    # TODO Replace fixed brokerage fee
    brokerage_fee = 6.95
    last_price = get_last_price(ticker_symbol)
    transaction_cost = (last_price * float(trade_volume)) + brokerage_fee
    if transaction_cost <= user_balance:
        # TODO unit price to be stored in a different column, so it's possible
        # to identify the price of the stock without fee
        #
        # Inserts order
        unit_cost = transaction_cost / float(trade_volume)
        mapper.insert_order(username,
                            ticker_symbol,
                            datetime.now(),
                            'B',
                            unit_cost,
                            trade_volume)
        # TODO Make inserts/updates in both tables be part of the same DB transaction.
        #
        # Inserts/Updates holdings
        update_user_holdings(username, ticker_symbol,
                             trade_volume, unit_cost, 'B')
        new_balance = user_balance - (trade_volume * unit_cost)
        update_user_balance(username, new_balance)
        return 'SUCCESS'
    else:
        # TODO Improve return so could show current balance and transaction cost.
        return 'NO_FUNDS'


def sell(ticker_symbol, trade_volume, username):
    user_balance = get_user_balance(username)
    #holdings = get_user_holdings_by_symbol(username, ticker_symbol)
    holding_volume = get_holding_volume_by_symbol(username, ticker_symbol)
    # if holdings != None:
    #holding_volume = holdings["volume"]
    # TODO Replace fixed brokerage fee
    brokerage_fee = 6.95
    last_price = get_last_price(ticker_symbol)
    transaction_income = (last_price * float(trade_volume)) - brokerage_fee
    if holding_volume >= trade_volume:
        # TODO unit price to be stored in a different column, so it's possible
        # to identify the price of the stock without fee
        #
        # Inserts order
        unit_price = transaction_income / float(trade_volume)
        mapper.insert_order(username,
                            ticker_symbol,
                            datetime.now(),
                            'S',
                            unit_price,
                            trade_volume)
        # TODO Make inserts/updates in both tables be part of the same DB transaction.
        #
        # Inserts/Updates holdings
        update_user_holdings(username, ticker_symbol,
                             trade_volume, unit_price, 'S')
        new_balance = user_balance + (trade_volume * unit_price)
        update_user_balance(username, new_balance)
        return 'SUCCESS'
    else:
        # TODO Improve return so could show current balance and transaction cost.
        return 'NO_FUNDS'


def get_last_price(ticker_symbol):
    return wrapper.get_last_price(ticker_symbol)


def get_ticker_symbol(company_name):
    return wrapper.get_ticker_symbol(company_name)


if __name__ == '__main__':
    # Test:
    # - Buy one share of AT&T at fair value (last price).
    #print(buy('t', 1, 'odisi'))
    pass
