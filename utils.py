from os import getenv
import json
from db import DBController as database

class UtilController:
    def __init__(self):
        self.db = database()
    def load_movies_from_json():
        with open('movies.json') as movie_json:
            data = json.load(movie_json)
        return data['movies']
    def load_movie_ids_from_json():
        with open('data.json') as movie_json:
            data = json.load(movie_json)
        return data['movies']
    def create_api_link(movieId):
        API_KEY = getenv('TMDB_API_KEY')
        root_url = "https://api.themoviedb.org/3"
        api_key = f"?api_key={API_KEY}"
        movie_info_url = f"{root_url}/movie/{movieId}{api_key}"
        return movie_info_url
    def generate_api_link_list(self, movies):
        api_links = []
        for m in movies:
            api_links.append(self.create_api_link(m))
        return api_links
    def build_movie_from_json(movie):
        movie = {
            "id": movie['id'],
            "title": movie['original_title'],
            "genre": [x for x in movie['genres']],
            "summary": movie['overview'],
            "total_votes": movie['vote_count'],
            "rating": movie['vote_average']
            }
        return movie