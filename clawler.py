from bs4 import BeautifulSoup
from datetime import datetime

TARGET_URL = 'https://zaif.jp/instant_exchange_btc_jpy/1'

def get_soup(url, http):
  html = http.request('GET', url).data
  soup = BeautifulSoup(html, 'html.parser')
  return soup

def get_bitcoin_price(http, url=TARGET_URL):
    """ ask: buy, bid: sell """
    soup = get_soup(url, http)
    bid = soup.find(id='btc_bid').get_text()
    ask = soup.find(id='btc_ask').get_text()
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return {'timestamp': now, 'bid': bid, 'ask': ask}
