#!/usr/bin/env python3

import model
import view


def login():
    username, pwd = view.login_menu()
    return model.login(username, pwd), username


def create_user():
    username, pwd = view.login_menu()
    model.create_user(username, pwd)


def game_loop(username):
    while True:
        # x = input('What do you want to do? ')
        buy_inputs = ['b', 'buy']
        sell_inputs = ['s', 'sell']
        lookup_inputs = ['l', 'lookup']
        quote_inputs = ['q', 'quote']
        balance_inputs = ['a', 'balance']
        exit_inputs = ['e', 'exit']
        acceptable_inputs = buy_inputs     \
            + sell_inputs   \
            + lookup_inputs \
            + quote_inputs \
            + balance_inputs  \
            + exit_inputs
        current_balance = model.get_user_balance(username)
        user_input = view.main_user_menu(username, current_balance)
        if user_input.lower() in acceptable_inputs:
            ###
            if user_input.lower() in buy_inputs:
                (ticker_symbol, trade_volume) = view.buy_menu()
                order_status = model.buy(ticker_symbol,
                                         int(trade_volume),
                                         username)
                if order_status == 'SUCCESS':
                    view.display_success()
                elif order_status == 'NO_FUNDS':
                    balance = model.get_user_balance(username)
                    view.display_insufficient_funds(balance)
            ###
            elif user_input.lower() in sell_inputs:
                (ticker_symbol, trade_volume) = view.sell_menu()
                order_status = model.sell(ticker_symbol,
                                          int(trade_volume),
                                          username)
                if order_status == 'SUCCESS':
                    view.display_success()
                elif order_status == 'NO_FUNDS':
                    holding_volume = model.get_holding_volume_by_symbol(
                        username, ticker_symbol)
                    view.display_insufficient_holdings(
                        ticker_symbol, holding_volume)
            elif user_input.lower() in lookup_inputs:
                company_name = view.lookup_menu()
                ticker_symbol = model.get_ticker_symbol(company_name)
                view.display_lookup(company_name, ticker_symbol)
                return ticker_symbol
            elif user_input.lower() in quote_inputs:
                ticker_symbol = view.quote_menu()
                last_price = model.get_last_price(ticker_symbol)
                view.display_last_price(ticker_symbol, last_price)
                return last_price
            elif user_input.lower() in balance_inputs:
                balance = model.get_user_balance(username)
                view.display_user_balance(username, balance)
            elif user_input.lower() in exit_inputs:
                view.exit_message()
                break
            else:
                view.display_invalid_menu_option()


if __name__ == '__main__':
    while True:
        try:
            choice = view.main_global_menu()
            if choice == '1':
                status, username = login()
                if status:
                    game_loop(username)
                else:
                    view.display_invalid_login()
            elif choice == '2':
                create_user()
                view.display_success()
            elif choice == '0':
                break
            else:
                view.display_invalid_menu_option()
        except Exception as e:
            view.display_error(e.args[0])
