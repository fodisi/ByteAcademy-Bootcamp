
#!/usr/bin/env python3

#Pseudocode

# Get all the links to each coin's, or token's, page listed on: http://api.bitcoincharts.com/v1/csv/
# -->if link == 'csv.gz'
# --> --> downloads the file

# Go to each one of the aforementioned pages and get the link to each coin's, or token's, source code

import os

from bs4 import BeautifulSoup
import requests


endpoint = "http://api.bitcoincharts.com/v1/csv/"

print('Making a request to the endpoint...\n')

#gets the html from endpoint
response = requests.get(endpoint).text
soup = BeautifulSoup(response, "html.parser")

# finds all possible references to links
links = soup.find_all("a")

print('Getting the links to the csv.gz file pages...\n')

for possible_link in links:
	#reads the link reference
	file_link = possible_link.get('href')
	#checks if the link is a .csv.gz file. If True, downloads the file.
	if file_link.lower().endswith('.csv.gz'):
		os.system('wget --user-agent="Mozilla/5.0" "{0}"'.format(endpoint + file_link))
