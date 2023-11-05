import openai

api_key='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'
openai.api_key = api_key

import csv
import openai

api_key='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'
openai.api_key = api_key

respuesta=openai.Completion.create(
    engine="davinci", #establecemos el motor, es decir, el modelo que vamos a utilizar
    prompt='creates a database with hundreds of wine, beer and cocktail options, with recommendations based on your pizza topping choices.',
    max_tokens=100,
)

texto_generado = respuesta.choices[0].text
print(texto_generado)

# Guarda los textos generados en un archivo CSV
with open('textos_generados.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Texto Generado"])  # Escribe la cabecera
    writer.writerow([texto_generado])
