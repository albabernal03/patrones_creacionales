<h1 align="center">Patrones creacionales</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/patrones_creacionales/tree/main)


<h2>¿De qué trata esta tarea?</h2>

<h3>Ejercicio1:</h3>

En este ejercicicio se nos pide que apliquemos el patron Abstract Factory para crear dos tipo de fábricas:

*Una fábrica que genere análisis estadísticos (media, moda, mediana).


*Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).

Para realizar un análisis de para modularizar y estandarizar el análisis de los datos que se nos proporcionan de Activaciones del SAMUR-Protección Civil.

<h3>Ejercicio 2</h3>

Este ejercicio implica diseñar un sistema para la cadena de pizzerías "Delizioso" que permita a los clientes personalizar sus pizzas de manera detallada. Se debe utilizar el patrón Builder para construir paso a paso las pizzas, validar las elecciones del cliente, incorporar recomendaciones basadas en elecciones anteriores, almacenar cada pizza en un archivo CSV, permitir la reconstrucción desde el archivo, asegurar flexibilidad para futuras actualizaciones, desarrollar una interfaz de usuario amigable y garantizar la seguridad de los datos. El uso del patrón Builder se justifica para lograr robustez y adaptabilidad, permitiendo la construcción flexible de pizzas complejas y facilitando futuras expansiones del sistema.

***

<h2>Indice</h2>

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)

***

## Ejercicio 1:<a name="id1"></a>

En primer lugar hacemos un análisis del CSV que se nos da:

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#-----------------------------------------
#leemos el dataset desde la url
#-----------------------------------------

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

#-----------------------------------------
#leemos el dataset
#-----------------------------------------
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

#-----------------------------------------
#Mostramos la información del dataset
#-----------------------------------------
data.info() #Esto nos sirve para ver el tipo de datos que tenemos en cada columna, y si nos aporta información relevante


#-----------------------------------------
#Ahora vamos a eliminar las columnas que no nos sirven para el análisis (columnas que tienen todos los valores nulos (NaN))
#-----------------------------------------

data.drop(['PRECIO', 'DIAS-EXCLUIDOS', 'DESCRIPCION', 'Unnamed: 29','GRATUITO'], axis=1, inplace=True)


"""
Como el dataset que se nos ha proporcionado contiene información 
sobre El SAMUR-Protección Civil que es es el servicio de atención a 
urgencias y emergencias sanitarias y se nos pide 
mostar la media de activaciones por día luego nuestra columna más relevante 
para ello sería la de FECHA.

"""



#-----------------------------------------
#Vamos a ver que valores estan mas relacionados con la columna FECHA
#-----------------------------------------


# Convertir la columna "FECHA" en numérica

data['FECHA'] = data['FECHA'].apply(lambda x: int("".join(x.split(" ")[0].split("-"))))

#Lo guardamos en un csv
#-----------------------------------------
data.to_csv('emergencias.csv', index=False)
print(data.columns)


#-----------------------------------------
#Hacer matrix de correlacion
#-----------------------------------------

# Calcular la matriz de correlación entre "FECHA" y otras variables numéricas
correlation_matrix = data.corrwith(data['FECHA'])

# Visualizar la matriz de correlación
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix.to_frame(), annot=True, cmap='coolwarm')
plt.title('Correlation con FECHA')
plt.show()
plt.savefig('correlation.png')

#-----------------------------------------
#Conclusiones
#-----------------------------------------

'''LUEGO DEL ANÁLISIS VEMOS QUE LA COLUMNA QUE MAYOR CORRELACION ES LA DE ID-EVENTO,
 POR LO QUE NOS CENTRAREMOS EN ANALIZAR AMBAS'''




```


