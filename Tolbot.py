import backoff
import requests
import json
import getpass
import urllib.parse

from requests.auth import HTTPDigestAuth
from pygerrit2 import GerritRestAPI, HTTPBasicAuth


@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

def get_change_files(change_id, revision_id, password):
    # Create an authentication object
    auth = HTTPBasicAuth('zrajrob', password)
    # Create a Gerrit REST API client
    rest = GerritRestAPI(url='***REMOVED***', auth=auth)
    endpoint = f"/changes/{change_id}/revisions/{revision_id}/files"
    response = rest.get(endpoint)
    return response

def get_file_diff(change_id, revision_id, file_path, password):
    # Create an authentication object
    auth = HTTPBasicAuth('zrajrob', password)
    # Create a Gerrit REST API client
    rest = GerritRestAPI(url='***REMOVED***', auth=auth)
    encoded_file_path = urllib.parse.quote(file_path, safe='')
    endpoint = f"/changes/{change_id}/revisions/{revision_id}/files/{encoded_file_path}/diff"
    response = rest.get(endpoint)
    return response


def main():
    print("Enter username:")
    username = getpass.getuser()
    print("username is", username)
    password = getpass.getpass(prompt="Enter Windows password: ")
    # print("Passoword is: ", password)
    changeId = input("Enter Change-Id:")
    REVISION_ID = 'd37bfc9f882b755d3b0dca53a01be8e0a896586d'
    try:
        files = get_change_files(changeId, REVISION_ID, password)
        print(files)
        keys = list(files.keys())
        print(keys) 
        for file_path in keys[1:]:
            print(f"Fetching diff for file: {file_path}")
            diff = get_file_diff(changeId, REVISION_ID, file_path, password)
            for key, value in diff.items():
                if key.startswith('content'):
                    for content in value:
                        # if 'a' in content:
                            # print(f"Original: {content['a']}")
                        if 'b' in content:
                            print(f"Modified: {content['b']}")
                        # if 'ab' in content:
                            # print(f"Common: {content['ab']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()