#!/usr/bin/env python3

import os


def wait_for_user():
    print('\n\n\nPress ENTER to continue...')
    input()


def display_header():
    os.system('clear')
    print('***********************')
    print('**                   **')
    print('*   Terminal Trader   *')
    print('**                   **')
    print('***********************\n')


def display_error(error):
    display_header()
    print('\n\n\nAn ERROR ocurred:')
    print('\n{0}'.format(error))
    wait_for_user()


def display_success():
    display_header()
    print('\n\n\nOperation executed successfully.')
    wait_for_user()


def display_invalid_menu_option():
    display_header()
    print('\n\n\nInvalid option. Try again.')
    wait_for_user()


def display_invalid_login():
    display_header()
    print('\n\n\nInvalid login.')
    wait_for_user()


def display_user_balance(username, balance):
    display_header()
    print('\n\n\n"{0}" has a balance of {1:.2f}'.format(
        username, balance)
    )
    wait_for_user()


def display_last_price(ticker_symbol, price):
    display_header()
    print('\n\n\nLast price for "{0}" is "{1:.2f}"'.format(
        ticker_symbol, price
    ))
    wait_for_user()


def display_lookup(company_name, ticker_symbol):
    display_header()
    print('\n\n\nSymbol of "{0}" is "{1}"'.format(
        company_name, ticker_symbol
    ))
    wait_for_user()


def display_insufficient_funds(balance):
    display_header()
    print('\n\n\nInsufficient funds. Your balance is {0:.2f}.'.format(balance))
    wait_for_user()


def display_insufficient_holdings(ticker_symbol, holding_volume):
    display_header()
    msg = '\n\n\nInsufficient holdings.\nYour holding volume for "{0}" is "{1:.2f}".'
    print(msg.format(ticker_symbol, holding_volume))
    wait_for_user()


def main_global_menu():
    display_header()
    print('\n\n\n1 - Login')
    print('2 - Create user')
    print('0 - Exit')
    return input('\n\n\nType your choice:      ')


def login_menu():
    display_header()
    username = input('Login: ')
    pwd = input('Password: ')
    return username, pwd


def main_user_menu(username, balance):
    display_header()
    print('Hello, {0}!'.format(username))
    print('Your balance is, {0:.2f}!'.format(balance))
    print('\n\nChoose an option:')
    print('b|buy     - Buy Stock')
    print('s|sell    - Sell Stock')
    print('l|lookup  - Lookup Stock Symbol')
    print('q|quote   - Stock Quote')
    print('a|balance - Balance')
    print('e|exit    - Exit')
    return input('\n\nType your option:     ')


def buy_menu():
    display_header()
    ticker_symbol = input('Ticker Symbol: ')
    trade_volume = input('Trade Volume: ')
    return ticker_symbol, trade_volume


def sell_menu():
    display_header()
    ticker_symbol = input('Ticker Symbol: ')
    trade_volume = input('Trade Volume: ')
    return ticker_symbol, trade_volume


def lookup_menu():
    display_header()
    company_name = input('Company Name: ')
    return company_name


def quote_menu():
    display_header()
    ticker_symbol = input('Ticker Symbol: ')
    return ticker_symbol


def exit_message():
    display_header()
    print('\n\n\nThanks for playing!')
    wait_for_user()


if __name__ == '__main__':
    print(buy_menu())
