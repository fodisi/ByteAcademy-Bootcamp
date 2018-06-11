#!/usr/bin/env python3


import mapper # import from local library or model
import wrapper


def get_and_record_price(ticker_symbol):
        last_price = wrapper.get_price(ticker_symbol)
        x = mapper.record_price(ticker_symbol, last_price)
        if x:
                return 'Done'
        else:
                return 'Error'

if __name__ == '__main__':
        print(get_and_record_price('tsla'))

