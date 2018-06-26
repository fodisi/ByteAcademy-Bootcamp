#!/usr/bin/env python3

import json
import sqlite3
from datetime import datetime

import requests

import mapper
import wrapper


""" Functions for Users. """


def create_user(username, password):
    return mapper.insert_user(username, password)


def update_balance(username, balance):
    return mapper.update_balance(username, balance)


def delete_user(username):
    return mapper.delete_user(username)


def login(username, password):
    user = mapper.select_user(username)
    if user != None:
        if (user['username'] == username) and (user['password'] == password):
            return user
    return None


def get_user_list():
    return mapper.select_all_users()


def get_current_balance(username):
    return mapper.select_current_balance(username)


""" Functions for Holdings. """


def get_holdings_by_symbol(username, ticker_symbol):
    return mapper.select_holdings_by_symbol(username, ticker_symbol)


def get_holding_volume_by_symbol(username, ticker_symbol):
    holding_volume = 0
    holdings = get_holdings_by_symbol(username, ticker_symbol)
    if holdings != None:
        holding_volume = holdings['volume']
    return holding_volume


def update_holdings(username, ticker_symbol, trade_volume, trade_unit_price, transaction_type):
    holdings = get_holdings_by_symbol(username, ticker_symbol)

    if holdings != None:
        if transaction_type == 'B':
            # finds the new weighted average unit price and new volume
            total_weighted_price = holdings['volume'] * \
                holdings['average_price']
            total_weighted_price += trade_volume * trade_unit_price
            total_volume = holdings['volume'] + trade_volume
            weighted_avg_price = total_weighted_price / float(total_volume)
            mapper.update_holdings(username,
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
            mapper.update_holdings(username,
                                   ticker_symbol,
                                   new_volume,
                                   holding_avg_price)
        else:
            raise Exception('Invalid transaction type')
    else:
        mapper.insert_holdings(username, ticker_symbol, trade_volume,
                               trade_unit_price)


def get_holdings_by_username(username):
    return mapper.select_holdings_by_username(username)


def get_holdings_with_market_value(username):
    brokerage_fee = 6.95
    mkt_holding_list = None
    user_holdings = get_holdings_by_username(username)
    if user_holdings != None:
        mkt_holding_list = []
        # Generates an updated holding list containing market price info
        for item in user_holdings:
            # Gets updated market price
            market_price = wrapper.get_last_price(item['ticker_symbol'])
            # Creates and fills holdings dictionary with updated market info
            mkt_holding = {}
            mkt_holding['pk'] = item['pk']
            mkt_holding['username'] = item['username']
            mkt_holding['ticker_symbol'] = item['ticker_symbol']
            mkt_holding['volume'] = item['volume']
            mkt_holding['avg_buy_price'] = item['average_price']
            mkt_holding['mkt_price'] = market_price
            ###### CALCULATES TOTALS AND DIFFERENCE ######
            # Total based on Buy Prices
            total_buy_price = item['volume'] * item['average_price']
            mkt_holding['total_buy_price'] = total_buy_price
            # Total based on Market Prices. Assumes one brokerage fee per holding.
            total_mkt_price = (item['volume'] * market_price) - brokerage_fee
            mkt_holding['total_mkt_price'] = total_mkt_price
            # Difference between market and buy price
            mkt_holding['difference'] = total_mkt_price - total_buy_price

            # Appends to the market holding list
            mkt_holding_list.append(mkt_holding)

    return mkt_holding_list


def get_realized_pl(username):
    initial, current = mapper.select_balance_for_pl(username)
    if initial > 0:
        pl = {}
        pl['username'] = username
        pl['initial_balance'] = initial
        pl['cur_balance'] = current
        pl['pl_value'] = current - initial
        pl['pl_percent'] = (current - initial) / initial * 100
        return pl
    else:
        return None


def get_account_data_by_user(username):
    realized_pl = get_realized_pl(username)
    mkt_holdings = get_holdings_with_market_value(username)
    initial_balance = 0
    cur_balance = 0
    real_pl = 0
    real_pl_perc = 0
    hold_buy_value = 0
    hold_mkt_value = 0
    account_real_value = 0
    account_mkt_value = 0
    unrealized_pl = 0
    unrealized_pl_perc = 0

    if realized_pl != None:
        # Calculates account and PL data
        initial_balance = realized_pl['initial_balance']
        cur_balance = realized_pl['cur_balance']
        real_pl = realized_pl['pl_value']
        real_pl_perc = realized_pl['pl_percent']

    if mkt_holdings != None:
        hold_buy_value = sum(item['total_buy_price'] for item in mkt_holdings)
        hold_mkt_value = sum(item['total_mkt_price'] for item in mkt_holdings)
        account_real_value = cur_balance + hold_buy_value
        account_mkt_value = cur_balance + hold_mkt_value
        unrealized_pl = account_mkt_value - initial_balance
        unrealized_pl_perc = unrealized_pl / initial_balance * 100

    # Fills object with account and PL data to be returned
    pl_data = {}
    pl_data['username'] = username
    pl_data['initial_balance'] = initial_balance
    pl_data['cur_balance'] = cur_balance
    pl_data['buy_hold_value'] = hold_buy_value
    pl_data['mkt_hold_value'] = hold_mkt_value
    pl_data['account_real_value'] = account_real_value
    pl_data['account_mkt_value'] = account_mkt_value
    pl_data['real_pl_value'] = real_pl
    pl_data['real_pl_percent'] = real_pl_perc
    pl_data['unreal_pl_value'] = unrealized_pl
    pl_data['unreal_pl_percent'] = unrealized_pl_perc
    pl_data['holdings'] = mkt_holdings

    return pl_data


def get_accounts_data():
    users = get_user_list()
    user_accounts = []
    for user in users:
        if user['profile'] == 'U':
            username = user['username']
            user_accounts.append(get_account_data_by_user(username))

    return user_accounts


""" Functions for Orders. """


def buy(ticker_symbol, trade_volume, username):
    # TODO Replace fixed brokerage fee
    brokerage_fee = 6.95

    user_balance = get_current_balance(username)
    last_price = get_last_price(ticker_symbol)
    transaction_cost = (last_price * float(trade_volume)) + brokerage_fee
    if transaction_cost <= user_balance:
        # TODO Make inserts/updates in both tables be part of the same DB transaction.

        # Inserts order
        mapper.insert_order(username,
                            ticker_symbol,
                            datetime.now(),
                            'B',
                            last_price,
                            trade_volume,
                            brokerage_fee)

        # Inserts/Updates holdings
        unit_cost = transaction_cost / float(trade_volume)
        update_holdings(username, ticker_symbol, trade_volume, unit_cost, 'B')

        # Updates balance
        # When buying, new balance must subtract transaction cost (including brokerage fee)
        new_balance = user_balance - transaction_cost
        update_balance(username, new_balance)

        return 'SUCCESS'
    else:
        # TODO Improve return so could show current balance and transaction cost.
        return 'NO_FUNDS'


def sell(ticker_symbol, trade_volume, username):
    # TODO Replace fixed brokerage fee
    brokerage_fee = 6.95

    user_balance = get_current_balance(username)
    holding_volume = get_holding_volume_by_symbol(username, ticker_symbol)
    last_price = get_last_price(ticker_symbol)
    transaction_value = (last_price * float(trade_volume)) - brokerage_fee
    if holding_volume >= trade_volume:
        # TODO Make inserts/updates in tables be part of the same DB transaction.

        # Inserts order
        mapper.insert_order(username,
                            ticker_symbol,
                            datetime.now(),
                            'S',
                            last_price,
                            trade_volume,
                            brokerage_fee)

        # Inserts/Updates holdings
        unit_price = transaction_value / float(trade_volume)
        update_holdings(username, ticker_symbol, trade_volume, unit_price, 'S')

        # When selling, new balance must sum up transaction value, excluding fees
        new_balance = user_balance + (transaction_value - brokerage_fee)
        update_balance(username, new_balance)

        return 'SUCCESS'
    else:
        # TODO Improve return so could show current balance and transaction cost.
        return 'NO_FUNDS'


def get_last_price(ticker_symbol):
    return wrapper.get_last_price(ticker_symbol)


def get_ticker_symbol(company_name):
    return wrapper.get_ticker_symbol(company_name)


def get_order_history(username):
    return mapper.select_order_history(username)


if __name__ == '__main__':
    # Test:
    # - Buy one share of AT&T at fair value (last price).
    #print(buy('t', 1, 'odisi'))
    pass
