import backoff
import requests
import urllib.parse
import sys
from pygerrit2 import GerritRestAPI, HTTPBasicAuth
import json

from ..Repository import Repository
from .Filter import Filter
from .TestStructureGetter import TestStructureGetter

@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

class GerritRepository(Repository):
 
    def __init__(self, server, change_id, revision_id, user):
        self.change_id = change_id
        self.revision_id = revision_id
        auth = HTTPBasicAuth(user['username'], user['password'])
        self.rest = GerritRestAPI(url=server, auth=auth)
    
    def get_tests(self):
        unfiltered_data = GerritRepository.get_unfiltered_diff_data(self)
        filter = Filter()
        filtered_data = filter.filter_data(unfiltered_data)

        test_structure_getter = TestStructureGetter()
        tests = test_structure_getter.get_structurized_tests_from_data(filtered_data)

        return tests

    def get_change_files(self):
        endpoint = f"/changes/{self.change_id}/revisions/{self.revision_id}/files"
        response = self.rest.get(endpoint)

        return response

    def get_file_diff(self, file_path):
        encoded_file_path = urllib.parse.quote(file_path, safe='')
        endpoint = f"/changes/{self.change_id}/revisions/{self.revision_id}/files/{encoded_file_path}/diff"
        response = self.rest.get(endpoint)

        return response

    def get_unfiltered_diff_data(self):
        unfiltered_data = []
        try:
            files = GerritRepository.get_change_files(self)
            keys = list(files.keys())
            for file_path in keys:
                if '/COMMIT_MSG' in file_path:
                    continue
                print(f"Fetching diff for file: {file_path}")
                diff = GerritRepository.get_file_diff(self, file_path)
                for key, value in diff.items():
                    if key.startswith('content'):
                        for content in value:
                            if 'b' in content:
                                for string in content['b']:
                                    unfiltered_data.append(string + '\n')
    
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit()
        return unfiltered_data
    
    def get_repo(self):
        endpoint = f"/changes/{self.change_id}/revisions/{self.revision_id}/review"
        response = self.rest.get(endpoint)

        project = response.get('project')
        return project
       

