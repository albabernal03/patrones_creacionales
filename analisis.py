import pandas as pd
mport mathplotlib.pyplot as plt

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"
# Leer CSV desde la URL

#leemos el dataset
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

#Mostramos la información del dataset
data.info() #Esto nos sirve para ver el tipo de datos que tenemos en cada columna, y si nos aporta información relevante

##Ahora vamos a eliminar las columnas que no nos sirven para el análisis (columnas que tienen todos los valores nulos (NaN))
data.drop(['PRECIO', 'DIAS-EXCLUIDOS', 'DESCRIPCION', 'Unnamed: 29'], axis=1, inplace=True)
print(data)

"""
Como el dataset que se nos ha proporcionado contiene información 
sobre El SAMUR-Protección Civil que es es el servicio de atención a 
urgencias y emergencias sanitarias y se nos pide 
mostar la media de activaciones por día luego nuestra columna más relevante 
para ello sería la de FECHA.

"""

#Ahora vamos a hacer una matriz de correlaciones para ver que columnas están más correlacionadas con la columna de FECHA
corr = data.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.show()
#Guardamos la imagen
plt.savefig("../imagenes/correlaciónvariables_fecha_.png")