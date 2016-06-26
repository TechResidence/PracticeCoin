import urllib3
from bs4 import BeautifulSoup

TARGET_URL = 'https://bitflyer.jp/'

def get_soup(url, http):
  html = http.request('GET', url).data
  soup = BeautifulSoup(html, 'html.parser')
  return soup

http = urllib3.PoolManager()
soup = get_soup(TARGET_URL, http)
soup.find(id='bfPriceAsk_0')




