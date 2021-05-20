from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode
import json
import sqlite3
import time
import re


SEARCH_URL='https://shop.boulderbar.net:8080/modules/bbext/CurrentCustomer.php#no-back-button'
AMOUNT_REGEX = '(?:<br/>)([\s\S]*?)(?=<br/>)'

page = requests.get(SEARCH_URL)
soup = BeautifulSoup(page.content, 'html.parser')
locations = soup.find_all('div', class_="progress-radial2")

output = [] 

for location in locations:
    name = location.find('h2').get_text()
    amount = re.findall(AMOUNT_REGEX, str(location))[0]
    output.append({name:amount})

print(json.dumps(output,indent=2))