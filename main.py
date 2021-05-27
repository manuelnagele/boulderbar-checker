#! /bin/python3

from bs4 import BeautifulSoup
import requests
import json
import re


SEARCH_URL='https://shop.boulderbar.net:8080/modules/bbext/CurrentCustomer.php#no-back-button'
AMOUNT_REGEX = '(?:<br/>)([\s\S]*?)(?=<br/>)'

page = requests.get(SEARCH_URL)
soup = BeautifulSoup(page.content, 'html.parser')
locations = soup.find_all('div', class_="progress-radial2")

output = {}

for location in locations:
    name = location.find('h2').get_text()
    amount = re.findall(AMOUNT_REGEX, str(location))[0]
    if amount[0] == 'ü':
        amount = amount.split(' ')[1]
    output[name] = int(amount)

print(json.dumps(output,indent=2))
