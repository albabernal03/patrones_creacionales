import openai

# Configura tu clave de API de OpenAI
api_key = "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"

# Define el texto de entrada con los ingredientes de la pizza
input_text = "Mi pizza tiene pepperoni, champiñones y aceitunas."

# Envía una solicitud al modelo para generar recomendaciones
response = openai.Completion.create(
    engine="text-davinci-002",  # O el motor que esté disponible en tu momento
    prompt=input_text,
    max_tokens=50  # Limita la longitud de la respuesta
)

# Obtiene la respuesta del modelo
recommendations = response.choices[0].text
print(recommendations)
