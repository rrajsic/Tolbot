
import backoff
import requests
from pygerrit2 import GerritRestAPI, HTTPBasicAuth

@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

class GerritConnection():
    def __init__(self, user):
        auth = HTTPBasicAuth(user['username'], user['password'])
        self.rest = GerritRestAPI(url='***REMOVED***', auth=auth)
    
    def get_rest(self):
        return self.rest

    def connect(self):
        try:
            response = self.rest.get('/config/server/version')
            print("Authentication successful")
            print(f"Gerrit server version: {response}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error connecting to Gerrit server: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Request timed out: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
        