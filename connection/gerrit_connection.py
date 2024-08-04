
import backoff
import requests
from pygerrit2 import GerritRestAPI, HTTPBasicAuth

@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

class GerritConnection():
    def __init__(self, user):
        self.user = user
        self.auth = HTTPBasicAuth(user['username'], user['password'])
        self.rest = GerritRestAPI(url='***REMOVED***', auth=self.auth)
    
    def get_rest(self):
        return self.rest

    def connect(self):
        try:
            response = self.rest.get('/config/server/version')
            print("Authentication successful")
            print(f"Gerrit server version: {response}")  
        except Exception as err:
            raise