#!/usr/bin/env python3 #shebang line
import os

from bs4 import BeautifulSoup
import requests

endpoint = "http://api.bitcoincharts.com/v1/csv/"

response = requests.get(endpoint).text

soup = BeautifulSoup(response, "html.parser")

links = soup.find_all('a')

market_data = []

for link in links:
	market_data.append(endpoint+link.get('href'))

	for _ in market_data:
		os.system('wget --user-agent="Mozilla/5.0" "{0}"'.format(_))

print(response)
