#!/usr/bin/env python3

#Pseudocode

# Get all the links to each coin's, or token's, page listed on: https://coinmarketcap.com/all/views/all/
# - Try getting all the links with the CSS class: currency-name-container
# -->if link_css_class == 'currency-name-container
# --> --> new_list.append(link_css_class)

# Go to each one of the aforementioned pages and get the link to each coin's, or token's, source code

import time

from bs4 import BeautifulSoup
import requests


endpoint = "https://coinmarketcap.com"
view_all = "/all/views/all/"

print('Making a request to the endpoint...\n')

response = requests.get(endpoint + view_all).text

soup = BeautifulSoup(response, "html.parser")

links = soup.find_all("a", class_='currency-name-container')

cryptocurrency_links = []

print('Getting the links to the CC pages...\n')

for link in links:
	cryptocurrency_links.append(endpoint + link.get('href'))

print('Getting the links to the source pages...\n')

for cryptocurrency_link in cryptocurrency_links:
	individual_response = requests.get(cryptocurrency_link).text
	individual_soup = BeautifulSoup(individual_response, 'html.parser')
	possible_links = individual_soup.find_all('a')
	for possible_link in possible_links:
		if possible_link.string == 'Source Code':
			print(possible_link.get('href'))

