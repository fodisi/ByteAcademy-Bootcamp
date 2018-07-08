#!usr/bin/env python3


from datetime import datetime

from core.wrapper.asset_wrapper import AssetWrapper


class Asset():

    def get_last_price(self, ticker_symbol):
        return AssetWrapper().get_last_price(ticker_symbol)

    def get_ticker_symbol(self, company_name):
        return AssetWrapper().get_ticker_symbol(company_name)
