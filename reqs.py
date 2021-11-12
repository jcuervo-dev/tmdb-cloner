import requests
from utils import UtilController as util

class RequestController:
    def request_url(url):
        response = requests.get(url)
        return response.json()
    def restart_request(url):
        RequestController.request_movie_from_api(url)
    def request_movie_from_api(self, url):
        self.url = url
        response = self.request_url(url)
        movie_dict = util.build_movie_from_json(response)
        return movie_dict