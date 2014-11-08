import json


def read_database(file_name):
        with open(file_name, 'r') as file_content:
            file_data = json.load(file_content)
        return file_data
