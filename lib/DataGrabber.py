import requests
from bs4 import BeautifulSoup
import cryptocurrencies

BASE_URL = 'http://coinmarketcap.com/currencies/'
CUR_URL = 'bitcoin' # This will be cycled
ATTR_URL = '/historical-data/?start=20130428&end=20200303'

def BrowserLaunch(self):
    limit = 1
    count = 1
    for coin in cryptocurrencies.cryptocurrencies:
        link = requests.get(BASE_URL+coin+ATTR_URL)
        html = requests.get(link) 
    return html

def PageParse(html):
    pages = BeautifulSoup(html,  'html.parser')
    table = pages.find_all('td', {"class":"cmc-table__cell"})
    # print(table[4].find("div", {"class": ""}).get_text())
    data = []
    for result in table:
        value=result.find("div",  {"class":""}).get_text()
        data.append(value)
    data2 = []
    for i in range(0,  1750,  7):
        date = data[i]
        price = data[i+4]
        ratio = (date,  price)
        data2.append(ratio)
    return data2
