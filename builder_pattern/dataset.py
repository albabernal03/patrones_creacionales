
import os
import openai
import requests
import json  # Importa el módulo JSON
import logging

# Obtén la clave de API desde la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Configura la clave de API de OpenAI
openai.api_key = api_key

# Define el encabezado de autorización
headers = {
    'Authorization': f'Bearer {api_key}',
}

# Define los datos de la solicitud en formato JSON
data = {
    'prompt': 'Mi pizza tiene pepperoni, champiñones y aceitunas.',
    'max_tokens': 5,
}

# Convierte los datos a formato JSON
data_json = json.dumps(data)

# Realiza la solicitud a la API
response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data_json)
logging.info(response.text)

# Imprime la respuesta
print(response.json())







#TODO: Arreglar esto