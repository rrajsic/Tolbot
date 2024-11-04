import backoff
import requests
import urllib.parse
import json

from requests.auth import HTTPBasicAuth
from ..Repository import Repository
from .SSLContextAdapter import SSLContextAdapter
import DEBUG_CONSTANTS

@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

class GtmsRepository(Repository):
    server = '***REMOVED***'
    client_cert = (DEBUG_CONSTANTS.CLIENT_CRT_FILE_PATH, DEBUG_CONSTANTS.CLIENT_KEY_FILE_PATH)
    ca_cert = DEBUG_CONSTANTS.CA_FILE_PATH
    pm_cert = DEBUG_CONSTANTS.PEM_FILE_PATH
    cer = DEBUG_CONSTANTS.CER_CHAIN_FILE_PATH
    ssl = DEBUG_CONSTANTS.SSL_CONTEXT
    chain = DEBUG_CONSTANTS.CER_CHAIN_FILE_PATH
    

    def __init__(self, user):
        auth = HTTPBasicAuth(user['username'], user['password'])

    def get_test_case_details(self, test_case_id, headers):
        url = f'***REMOVED***api/tcm/test-cases/{test_case_id}/export'
        response = requests.get(url, headers=headers, verify = self.chain)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get details for ID {test_case_id} with status code:", response.status_code)
            return None

    def get_tests(self, context_id, user):
        auth = HTTPBasicAuth(user['username'], user['password'])
        credentials = {
            "login": user['username'],
            "password": user['password']  # Replace with your actual password
        }
        login = requests.post(url="***REMOVED***api/auth/login", json=credentials, verify=self.chain)
        jwt = login.headers.get('Authorization')
 
        headers = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : jwt
        }
        
        response = requests.get(url='***REMOVED***api/tcs/selection-strategies/preview/f157f5c3-4352-4ce8-9d77-505ff5021e9d/previews-sp', headers=headers, verify =self.chain)
        
        if response.status_code == 200:
            response_json = response.json()
            ids = [item['id'] for item in response_json.get('data', []) if 'id' in item]
            
            tests = []
            for test_case_id in ids:
                tests.append(GtmsRepository.get_test_case_details(self, test_case_id, headers))
