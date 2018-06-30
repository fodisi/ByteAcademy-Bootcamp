#!/usr/bin/env python3

import json

import requests


class AssetWrapper():
    def get_last_price(self, ticker_symbol):
        try:
            # TODO Re-factor the following code so it doesn't just arbitrarily take the first
            endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='
            return json.loads(requests.get(endpoint + ticker_symbol).text)['LastPrice']
        except:
            msg = "Unable to get a price for symbol '{0}' on MarkitOnDemand API. Check your input and try again."
            raise Exception(msg.format(ticker_symbol))

    def get_ticker_symbol(self, company_name):
        # TODO Re-factor the following code so it doesn't just arbitrarily take the first
        try:
            endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='
            return json.loads(requests.get(endpoint + company_name).text)[0]['Symbol']
        except:
            msg = "Unable to get a ticker symbol for company '{0}' on MarkitOnDemand API. Check your input and try again."
            raise Exception(msg.format(company_name))


if __name__ == '__main__':
    wrapper = AssetWrapper()
    print(wrapper.get_ticker_symbol('tesla'))
    print(wrapper.get_last_price('tsla'))
