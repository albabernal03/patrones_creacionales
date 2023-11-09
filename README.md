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
A continuación pasamos a construir el patrón, en este caso emplearemos el patron creacional Abstract Factory:

```
from abc import ABC, abstractmethod

#-----------------------------------------
#AbstractProductA
#-----------------------------------------

class CalculosEstadisticos(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass
```

```
from abc import ABC, abstractmethod

#-----------------------------------------
#AbstractProductB
#-----------------------------------------

class Graficas(ABC):
    @abstractmethod
    def grafica(self) -> None:
        pass


```

```
from abc import ABC, abstractmethod
from calculosestadisticos import CalculosEstadisticos
from graficas import Graficas


#-----------------------------------------
#AbstractFactory
#-----------------------------------------

class Analisisdatos(ABC):
    @abstractmethod
    def crear_calculos(self) -> CalculosEstadisticos:
        pass

    @abstractmethod
    def crear_graficas(self) -> Graficas:
        pass

```

```
from calculosestadisticos import CalculosEstadisticos
import pandas as pd
from numpy import mean

#-----------------------------------------
#ConcreteProductA1
#-----------------------------------------
class Media(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        activaciones_por_dia = datos.groupby(datos['FECHA']).size()
        return (f'La media es: {activaciones_por_dia.mean()}')
```

```
from calculosestadisticos import CalculosEstadisticos
import pandas as pd
from statistics import mode
#-----------------------------------------
#ConcreteProductA2
#-----------------------------------------

class Moda(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        activaciones_por_dia = datos.groupby(datos['FECHA']).size()
        return (f'La moda es: {mode(activaciones_por_dia)}')

```

```
from calculosestadisticos import CalculosEstadisticos
import pandas as pd
from numpy import median


#-----------------------------------------
#ConcreteProductA3
#-----------------------------------------

class Mediana(CalculosEstadisticos):
    def calcular(self) -> float:
        datos=pd.read_csv("emergencias.csv")
        activaciones_por_dia = datos.groupby(datos['FECHA']).size()
        return (f'La mediana es: {activaciones_por_dia.median()}')
    


```

```
from graficas import Graficas
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------
#ConcreteProductB1
#-----------------------------------------

class Histograma(Graficas):
    def grafica(self) -> None:
        data = pd.read_csv('emergencias.csv')
        plt.hist(data['TITULO'])
        plt.xticks(rotation=90)
        plt.xlabel('Eventos')
        plt.ylabel('Número de evento')
        plt.title('Número de Activaciones por Evento')
        plt.show()
       
```
```
from graficas import Graficas
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------
#ConcreteProductB2
#-----------------------------------------

class GraficaBarras(Graficas):
    def grafica(self) -> None:
        data = pd.read_csv('emergencias.csv')
        # Agrupar por fecha y contar las activaciones por día
        activaciones_por_dia = data.groupby(data['FECHA']).size()
        # Visualizar el número de activaciones por día
        activaciones_por_dia.plot(kind='bar', figsize=(10, 6))
        plt.xlabel('Fecha')
        plt.ylabel('Número de Activaciones')

        plt.title('Número de Activaciones por Día')
        plt.show()
```

```
from analisisdatos_factory import Analisisdatos
from media import Media
from moda import Moda
from mediana import Mediana
from calculosestadisticos import CalculosEstadisticos
from graficas import Graficas


#-----------------------------------------
#ConcreteFactory1
#-----------------------------------------

class Calculosmmm(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return [Media(), Mediana(), Moda()]

    def crear_graficas(self) -> Graficas:
        return None


```

```
from calculosestadisticos import CalculosEstadisticos
from graficas import Graficas
from analisisdatos_factory import Analisisdatos
from barras import GraficaBarras
from histograma import Histograma

#-----------------------------------------
#ConcreteFactory2
#-----------------------------------------

class Mostrargraficas(Analisisdatos):
    def crear_calculos(self) -> CalculosEstadisticos:
        return None

    def crear_graficas(self) -> Graficas:
        return [GraficaBarras(), Histograma()]



```

```
from calculosmmm_factory import Calculosmmm
from mostrargraficas_factory import Mostrargraficas

#-----------------------------------------
#Client
#-----------------------------------------


def main():
    factory=Calculosmmm()

    calculos=factory.crear_calculos()

    for i in calculos:
        print(i.calcular())

    factory=Mostrargraficas()

    mostrar=factory.crear_graficas()

    for i in mostrar:
        i.grafica()


if __name__ == "__main__":
    main()
   
```


Al ejecutarlo obtenemos por consola lo siguiente:

<img width="529" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/210ba387-fa3e-4ff5-a134-dddfe48871b1">

<img width="496" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/db6453a1-d36e-48c8-98c5-1069f009094c">

![histograma](https://github.com/albabernal03/patrones_creacionales/assets/91721875/e4a1232d-e6b8-44da-965f-9a090b14981b)



