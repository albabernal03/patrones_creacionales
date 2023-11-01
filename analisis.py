import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"
# Leer CSV desde la URL

#leemos el dataset
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

#Mostramos la información del dataset
data.info() #Esto nos sirve para ver el tipo de datos que tenemos en cada columna, y si nos aporta información relevante

##Ahora vamos a eliminar las columnas que no nos sirven para el análisis (columnas que tienen todos los valores nulos (NaN))
data.drop(['PRECIO', 'DIAS-EXCLUIDOS', 'DESCRIPCION', 'Unnamed: 29','GRATUITO'], axis=1, inplace=True)
print(data)

"""
Como el dataset que se nos ha proporcionado contiene información 
sobre El SAMUR-Protección Civil que es es el servicio de atención a 
urgencias y emergencias sanitarias y se nos pide 
mostar la media de activaciones por día luego nuestra columna más relevante 
para ello sería la de FECHA.

"""


data.to_csv('emergencias.csv', index=False)
# Convertir la columna de fecha en formato datetime
data['FECHA'] = pd.to_datetime(data['FECHA'])
# Extraer el día de la semana de la columna "FECHA"
data['DIA_SEMANA'] = data['FECHA'].dt.dayofweek
# Crear variables ficticias para el día de la semana y asignar los nombres deseados
variables_ficticias = pd.get_dummies(data['DIA_SEMANA']).rename(columns={
    0: 'Lunes',
    1: 'Martes',
    2: 'Miércoles',
    3: 'Jueves',
    4: 'Viernes',
    5: 'Sábado',
    6: 'Domingo'
})

# Concatenar las variables ficticias al dataframe original
data = pd.concat([data, variables_ficticias], axis=1)

# Calcular la matriz de correlación
matriz_correlacion = data.corr()

# Mostrar la matriz de correlación
print(matriz_correlacion)

# Crear una nueva columna numérica con la fecha convertida
data['FECHA_NUM'] = data['FECHA'].apply(lambda x: x.toordinal())

# Calcular la matriz de correlaciones
corr = data.corr()

# Visualizar la matriz de correlaciones
plt.figure(figsize=(10,10)) 
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.show()

# Guardar la imagen de la matriz de correlaciones
plt.savefig('matriz_correlaciones.png')


#LUEGO DEL ANÁLISIS VEMOS QUE LA COLUMNA QUE MAYOR CORRELACION ES LA DE ID-EVENTO, POR LO QUE NOS CENTRAREMOS EN ANALIZAR AMBAS