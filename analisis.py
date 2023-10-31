import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"
# Leer CSV desde la URL

#leemos el dataset
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

#Mostramos la información del dataset
data.info()

