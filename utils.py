import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'lxml')
    return soup
