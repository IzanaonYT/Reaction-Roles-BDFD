import requests

# URL base del servidor FastAPI
base_url = "http://localhost:8000/api/reaction-roles-delete/1/"

# Datos para la solicitud

# Solicitud POST para actualizar los roles
response = requests.delete(base_url)

print(response.status_code)

