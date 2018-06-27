#!/usr/bin/env python3

import json

import requests


class AssetWrapper():
    def get_last_price(self, ticker_symbol):
        try:
            endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='
            return json.loads(requests.get(endpoint + ticker_symbol).text)['LastPrice']
        except:
            msg = 'markitondemand API did not return a price for {0}. Please try again.'
            raise Exception(msg.format(ticker_symbol))

    def get_ticker_symbol(self, company_name):
        # TODO Re-factor the following code so it doesn't just arbitrarily take the first
        try:
            endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='
            return json.loads(requests.get(endpoint + company_name).text)[0]['Symbol']
        except:
            msg = 'markitondemand API did not return a ticker symbol for {0}. Please try again.'
            raise Exception(msg.format(company_name))


if __name__ == '__main__':
    wrapper = AssetWrapper()
    print(wrapper.get_ticker_symbol('tesla'))
    print(wrapper.get_last_price('tsla'))
