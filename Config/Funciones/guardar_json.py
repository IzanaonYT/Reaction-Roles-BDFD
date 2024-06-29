import json

def save_data(data):
    with open('roles.json', 'w') as file:
        json.dump(data, file, indent=4)