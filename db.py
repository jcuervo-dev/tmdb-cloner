import pymongo
from os import getenv
import json

# Remote mongodb url
MONGODB_URL = getenv('MONGODB_URL')

# Local mongodb url 'mongo:localhost:27017'
# MONGODB_URL = getenv('MONGODB_LOCAL')


class DBController:
    def __init__(self):
        self.client = pymongo.MongoClient(f"{MONGODB_URL}")
        self.db = self.client['moviejunky']
        self.movies =  self.db['movies']
    
    def get_all_movie_ids(self):
        movie_ids = self.movies.find({}, {'id': 1, '_id': 0})
        movie_ids = [x['id'] for x in movie_ids]
        return movie_ids
    
    def insert_movie_from_dict(self, data):
        x = self.movies.insert_one(data)
    def bulk_insert_movies_from_list(self, data):
        x = self.movies.insert_many(data)
    def search_movie_with_index(self, id):
        if(self.movies.find({'id': id }).count() > 0):
            self.client.close()
            return True
        else:
            self.client.close()
            return False