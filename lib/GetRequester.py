import requests
import json

class GetRequester: # Start by creating a GetRequester class. This class should be able to initialize with a string URL.

    def __init__(self, url):
        self.url = url

    def get_response_body(self): # The GetRequester class should have a get_response_body method that sends a GET request to the URL passed in on initialization. This method should return the body of the response.
        response = requests.get(self.url)
        return response.content

    def load_json(self): # The GetRequester class should have a load_json method that should use get_response_body to send a request, then return a Python list or dictionary made up of data converted from the response of that request.
        return json.loads(self.get_response_body())
        
