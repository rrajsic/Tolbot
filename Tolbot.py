import backoff
import requests
import json
import urllib.parse
import os

import formatter
import DEBUG_CONSTANTS


@backoff.on_exception(backoff.expo, 
                      requests.exceptions.ConnectionError,
                      max_time=10)

def get_change_files(change_id, revision_id, password):
    endpoint = f"/changes/{DEBUG_CONSTANTS.CHANGE_ID}/revisions/{DEBUG_CONSTANTS.REVISION_ID}/files"
    response = rest.get(endpoint)
    return response

def get_file_diff(change_id, revision_id, file_path, password):
    encoded_file_path = urllib.parse.quote(file_path, safe='')
    endpoint = f"/changes/{change_id}/revisions/{revision_id}/files/{encoded_file_path}/diff"
    response = rest.get(endpoint)
    return response


def main():
    print("Enter username:")
    print("username is", DEBUG_CONSTANTS.USERNAME)
    # password = getpass.getpass(prompt="Enter Windows password: ")
    # print("Passoword is: ", password)
    # changeId = input("Enter Change-Id:")
   
    try:
        files = get_change_files(DEBUG_CONSTANTS.CHANGE_ID, REVISION_ID, DEBUG_CONSTANTS.PASSWORD)
        print(files)
        keys = list(files.keys())
        print(keys) 
        # Open the file with determined mode
        with open(DEBUG_CONSTANTS.FILENAME, 'w') as file:
            for file_path in keys:
                print(f"Fetching diff for file: {file_path}")
                diff = get_file_diff(DEBUG_CONSTANTS.CHANGE_ID, REVISION_ID, file_path, DEBUG_CONSTANTS.PASSWORD)
                for key, value in diff.items():
                    if key.startswith('content'):
                        for content in value:
                            if 'b' in content:
                                for string in content['b']:
                           
                                    file.writelines(string + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")
    formatter.format(DEBUG_CONSTANTS.FILENAME)

if __name__ == "__main__":
    main()