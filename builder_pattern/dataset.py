import os 
import openai
import requests
import os

# Obtén la clave de API desde la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Configura la clave de API de OpenAI
openai.api_key = api_key

#Definimos el encabezado de la autorización

headers = {
    'Authorization':f'Bearer {api_key}',
}

#Definimos los datos de la solicitud 

data = {
    'prompt': 'Mi pizza tiene pepperoni, champiñones y aceitunas.',
    'max_tokens': 5,
}

# Realiza la solicitud a la API
response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, data=data)

#Imprimimos la respuesta
print(response.json())


