import json

class JSONHandler():
    def __init__(self, file_name):
        self.file_name = file_name

    def export_to_json(self, data):
        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file)  
    
    def import_from_json(self):
        with open(self.file_name, "r") as json_file:
            data = json.load(json_file)
        return data