from bs4 import BeautifulSoup
import requests


def get_proxies():
    url = 'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    proxies = []
    for i in soup.select(".blob-code.blob-code-inner.js-file-line"):
        proxies.append(i.text)
    return proxies