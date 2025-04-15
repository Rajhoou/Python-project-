

import json

def save_data_to_file(data, filename="students.json"):
    with  open(filename, "w") as file:
        json.dump(data, file)
        print("Data saved successfully!")

def load_data_from_file(filename="students.json"):
    try:
        with open(filename, "r") as file:
            return  json.load(file)
    except FileNotFoundError:
        print("File not found. Starting with an empty database.")
        return {}
    
    students  =  load_data_from_file()  