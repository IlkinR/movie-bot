from collections import namedtuple

import aiohttp
import lxml as lxml
import requests
from bs4 import BeautifulSoup
import lxml

Movie = namedtuple('Movie', ['title', 'year'])

url = 'https://www.whatismymovie.com/results?text=movie+where+man+kills+super+hero'


def get_soup(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'lxml')
    return soup


def get_movies(url):
    soup = get_soup(url)
    movie_tags = soup.find_dall('h3', class_='panel-title')
    movies = [tag.text.split('(') for tag in movie_tags][::2]
    return [
        Movie(title=title.strip(), year=year[:-1])
        for title, year in movies
    ]
