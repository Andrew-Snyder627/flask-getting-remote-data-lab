import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Make a GET request to the URL and return raw content
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Make a GET request and parse the JSON into Python data
        response = requests.get(self.url)
        return response.json()
