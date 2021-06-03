from collections import namedtuple
from utils import get_soup

Movie = namedtuple('Movie', ['title', 'year'])


class MovieParser:
    MOVIE_URL_TEMPLATE = 'https://www.whatismymovie.com/results?text={query}'
    MOVIE_URL_JOINER = '+'

    @classmethod
    def _get_url(cls, user_query: str) -> str:
        return cls.MOVIE_URL_TEMPLATE.format(
            query=cls.MOVIE_URL_JOINER.join(user_query.split())
        )

    @classmethod
    def _parse_movie(cls, movie_tag) -> Movie:
        movie_data = movie_tag.text.split('(')
        return Movie(
            title=movie_data[0].strip(),
            year=movie_data[1]
        )

    def __init__(self, desired_movie: str):
        soup = get_soup(MovieParser._get_url(desired_movie))
        self.movie_tags = soup.select('h3.panel-title')[::2]

    def parse(self):
        return [
            MovieParser._parse_movie(tag)
            for tag in self.movie_tags
        ]
