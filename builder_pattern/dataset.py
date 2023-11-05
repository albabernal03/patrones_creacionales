import os
import openai
import time

os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = os.environ['OPENAI_API_KEY']

question = 'creates a database with hundreds of wine, beer and cocktail options, with recommendations based on your pizza topping choices.'

# Controla la velocidad de las solicitudes
def generar_respuesta():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              temperature=0,
                                              messages=[{"role": "user", "content": question}])
    respuesta = completion["choices"][0]["message"]["content"]
    return respuesta

if __name__ == "__main__":
    while True:
        respuesta = generar_respuesta()
        print(respuesta)

        # Espera para cumplir con los límites de 3 RPM
        time.sleep(20)  # Espera 20 segundos entre solicitudes
