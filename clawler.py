import urllib3
from bs4 import BeautifulSoup
import time
from datetime import datetime
TARGET_URL = 'https://zaif.jp/instant_exchange_btc_jpy/1'

def get_soup(url, http):
  html = http.request('GET', url).data
  soup = BeautifulSoup(html, 'html.parser')
  return soup

# ask: buy, bid: sell
def get_bitcoin_price(url=TARGET_URL):
  http = urllib3.PoolManager()
  while True:
    soup = get_soup(url, http)
    bid = soup.find(id='btc_bid').get_text()
    ask = soup.find(id='btc_ask').get_text()
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    time.sleep(2)
    print(now, 'bid: ', bid, 'ask: ', ask)


get_bitcoin_price()
