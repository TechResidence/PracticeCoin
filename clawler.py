import urllib3
from bs4 import BeautifulSoup

TARGET_URL = 'https://zaif.jp/instant_exchange_btc_jpy/1'

def get_soup(url, http):
  html = http.request('GET', url).data
  soup = BeautifulSoup(html, 'html.parser')
  return soup

http = urllib3.PoolManager()
soup = get_soup(TARGET_URL, http)
bid = soup.find(id='btc_bid').get_text()
ask = soup.find(id='btc_ask').get_text()

print("bid: ", bid, "ask: ", ask)

