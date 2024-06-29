import json

def load_data():
    try:
        with open('roles.json', 'r') as file:
            data = json.load(file)
            if not data:
                return {"reacion": []}  # O cualquier estructura predeterminada
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"reacion": []}  # Manejar el caso de archivo vacío o no válido