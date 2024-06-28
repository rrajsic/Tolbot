import backoff
import requests
import json
import urllib.parse
import sys

import DEBUG_CONSTANTS

@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

def get_change_files(change_id, revision_id, password):
    endpoint = f"/changes/{change_id}/revisions/{revision_id}/files"
    response = DEBUG_CONSTANTS.rest.get(endpoint)
    return response

def get_file_diff(change_id, revision_id, file_path, password):
    encoded_file_path = urllib.parse.quote(file_path, safe='')
    endpoint = f"/changes/{change_id}/revisions/{revision_id}/files/{encoded_file_path}/diff"
    response = DEBUG_CONSTANTS.rest.get(endpoint)
    return response

def get_unfiltered_diff_data():
    unfiltered_data = []
    try:
        files = get_change_files(DEBUG_CONSTANTS.CHANGE_ID, DEBUG_CONSTANTS.REVISION_ID, DEBUG_CONSTANTS.PASSWORD)
        keys = list(files.keys())
        for file_path in keys:
            print(f"Fetching diff for file: {file_path}")
            diff = get_file_diff(DEBUG_CONSTANTS.CHANGE_ID, DEBUG_CONSTANTS.REVISION_ID, file_path, DEBUG_CONSTANTS.PASSWORD)
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