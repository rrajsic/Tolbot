import json

class ServerConfig():
    def __init__(self, file_name):
        self.file_name = file_name

    def import_from_json(self):
        try:
            with open(self.file_name, "r") as json_file:
                data = json.load(json_file)
                servers = data["servers"]
            return servers
        except FileNotFoundError:
            print("The file 'servers_config.json' was not found.")
            return ["N/A"]
        except json.JSONDecodeError:
            print("Failed to decode JSON. The file may be corrupted or improperly formatted.")
            return ["N/A"]
        except IOError as e:
            print(f"An I/O error occurred: {e}")
            return ["N/A"]