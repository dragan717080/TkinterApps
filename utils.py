import json
from abc import ABC

class Utils(ABC):

    @staticmethod
    def read_json_file(file_name, file_path='data/'):
        with open(f'{file_path}{file_name}.json', 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def get_first_letters(string, lower=None):
        words = string.split()
        first_letters = [word[0] for word in words]
        result = ''.join(first_letters)
        return result if lower is not None else result.lower()
