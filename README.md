<h1 align="center">Patrones creacionales</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/patrones_creacionales/tree/main)


<h2>¿De qué trata esta tarea?</h2>

<h3>Ejercicio 1:</h3>

En este ejercicicio se nos pide que apliquemos el patron Abstract Factory para crear dos tipo de fábricas:

*Una fábrica que genere análisis estadísticos (media, moda, mediana).


*Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).

Para realizar un análisis de para modularizar y estandarizar el análisis de los datos que se nos proporcionan de Activaciones del SAMUR-Protección Civil.

<h3>Ejercicio 2:</h3>

Este ejercicio implica diseñar un sistema para la cadena de pizzerías "Delizioso" que permita a los clientes personalizar sus pizzas de manera detallada. Se debe utilizar el patrón Builder para construir paso a paso las pizzas, validar las elecciones del cliente, incorporar recomendaciones basadas en elecciones anteriores, almacenar cada pizza en un archivo CSV, permitir la reconstrucción desde el archivo, asegurar flexibilidad para futuras actualizaciones, desarrollar una interfaz de usuario amigable y garantizar la seguridad de los datos. El uso del patrón Builder se justifica para lograr robustez y adaptabilidad, permitiendo la construcción flexible de pizzas complejas y facilitando futuras expansiones del sistema.


<h3>Ejercicio 3:</h3>

En este ejercicio, la cadena "Delizioso" busca expandir su plataforma digital de creación de pizzas gourmet, ahora permitiendo a los clientes combinar sus pizzas personalizadas con entradas, bebidas y postres en menús personalizados. Se propone introducir la noción de menús simples o compuestos, cada uno con un código único y precio calculado según la suma de los elementos con descuentos aplicados. Para gestionar esta complejidad, se sugiere implementar el patrón Composite, modelando las relaciones entre elementos y menús. Además, se continuará utilizando el patrón Builder para la creación detallada de pizzas y se ampliará la interacción con archivos CSV para almacenar y recuperar información de menús. La eficiencia en el cálculo de precios de menús es una prioridad, y se espera un diseño modular y orientado a objetos con clara separación de responsabilidades.

***
<h3>Ejercicio 4:</h3>

<h2>Indice</h2>

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Implementacion del ejercicio 2 en una página web](#id3)
4. [¿Por qué usamos elpatrón Builder?](#id4)
5. [Ejercicio 3](#id5)

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
La matriz de correlacion que se obtiene es la siguiente:


![correlacion](https://github.com/albabernal03/patrones_creacionales/assets/91721875/c6d17798-785c-4139-b44a-6e168c75c070)


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

<img width="234" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/6e2870d5-42a7-4c26-9d19-ef96349a094a">



<img width="319" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/491ecced-2139-4d6f-b1ce-df714cad624c">


![grafica](https://github.com/albabernal03/patrones_creacionales/assets/91721875/aa767936-af73-4a32-b223-ea5efa4bfab3)

***

## Ejercicio 2:<a name="id2"></a>

En este ejercicio diseñamos una pizzeria haciendo uso del patron creacional Builder

```
from abc import ABC, abstractmethod

#-----------------------------------------
#Abstract Builder
#-----------------------------------------

class PizzaBuilder(ABC):

    @abstractmethod
    def añadir_masa(self):
        pass

    @abstractmethod
    def añadir_salsa(self):
        pass

    @abstractmethod
    def añadir_ingredientes_principales(self):
        pass

    @abstractmethod
    def añadir_coccion(self):
        pass

    @abstractmethod
    def añadir_presentacion(self):
        pass

    @abstractmethod
    def añadir_maridaje_recomendado(self):
        pass

    @abstractmethod
    def añadir_extra(self):
        pass
```

```
from pizza_builder import PizzaBuilder 
from pizza import Pizza

#-----------------------------------------
#Concrete Builder
#-----------------------------------------

class PizzaCustomizadaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def añadir_masa(self):
        self.pizza.masa= input('¿Qué masa quieres? fina o gruesa: ')

    def añadir_salsa(self):
        self.pizza.salsa= input('¿Qué salsa quieres? tomate o barbacoa: ')

    def añadir_ingredientes_principales(self):
        opciones_ingredientes = ['tomate', 'queso', 'jamon', 'atun', 'champiñones', 'bacon', 'cebolla', 'pollo', 'piña',
                                 'aceitunas', 'anchoas', 'maiz', 'salchichas', 'pimiento', 'gambas', 'carne picada', 'huevo']
        
        print("Elige los ingredientes principales para tu pizza:")
        for i, ingrediente in enumerate(opciones_ingredientes, start=1):
            print(f"{i}. {ingrediente}")

        seleccionados = input("Ingresa los números de los ingredientes separados por comas: ")
        numeros_seleccionados = [int(x) for x in seleccionados.split(',') if x.isdigit()]

        ingredientes_seleccionados = [opciones_ingredientes[i - 1] for i in numeros_seleccionados]

        self.pizza.ingredientes_principales = ingredientes_seleccionados

    def añadir_coccion(self):
        self.pizza.coccion= input('¿Cómo quieres que se cocine? al horno o a la piedra: ')

    def añadir_presentacion(self):
        self.pizza.presentacion= input('¿Cómo quieres que se presente? entera o en porciones: ')

    def añadir_maridaje_recomendado(self):
        bebidas={
            'cerveza': ['pollo', 'bacon', 'salchichas', 'carne picada', 'huevo', 'queso'],
            'vino blanco': ['gambas', 'atun', 'anchoas','queso', 'champiñones'],
            'vino_tinto': ['queso', 'aceitunas', 'tomate', 'maiz', 'champiñones', 'pimiento'],
            'sangria': ['pollo', 'bacon', 'queso', 'huevo', 'atun', 'jamon', 'carne picada'],
            'cocacola': ['huevo', 'queso', 'jamon', 'bacon', 'champiñones', 'pollo', 'pimiento', 'carne picada', 'salchichas'],
            'fanta_naranja': ['aceitunas', 'atun', 'anchoas', 'maiz', 'gambas'],
            'fanta_limon': ['pollo', 'bacon', 'queso', 'salchichas', 'huevo', 'atun', 'jamon', 'carne picada', 'champiñones', 'pimiento'],
            'agua': ['pollo', 'bacon', 'queso', 'salchichas', 'huevo', 'atun', 'jamon', 'carne picada', 'champiñones', 'pimiento']

        }

        ingredientes_pizza = self.pizza.ingredientes_principales

        maridaje_recomendado= None
        max_coincidencias = 0

        for bebida, ingredientes_bebida in bebidas.items():
            coincidencias= len(set(ingredientes_pizza).intersection(ingredientes_bebida))
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                maridaje_recomendado = bebida

        print(f"El maridaje recomendado para tu pizza es: {maridaje_recomendado}")
        cambiar_maridaje = input('¿Quieres cambiar el maridaje recomendado? si o no: ')
        if cambiar_maridaje == 'si':
            self.pizza.maridaje_recomendado = input('¿Qué bebida quieres? cerveza, vino blanco, vino tinto, sangria, cocacola, fanta_naranja, fanta_limon o agua: ')
        else:
            self.pizza.maridaje_recomendado = maridaje_recomendado

    def añadir_extra(self):
        self.pizza.extra= input('¿Quieres bordes rellenos de queso? si o no: ')
        if self.pizza.extra == 'si':
            self.pizza.extra = 'bordes rellenos de queso'
        else:
            self.pizza.extra = 'sin bordes rellenos de queso'

```

```
#-----------------------------------------
#Product
#-----------------------------------------

class Pizza():
    def __init__(self):
        self.masa= ''
        self.salsa= ''
        self.ingredientes_principales= []
        self.coccion= [] 
        self.presentacion= ''
        self.maridaje_recomendado= ''
        self.extra= []

```

```

#-----------------------------------------
#Director
#-----------------------------------------

class PizzaDirector():
    def __init__(self):
        self.builder = None

    @property
    def builder(self)-> PizzaBuilder:
        return self._builder
    
    @builder.setter #este setter es para que el builder se pueda cambiar en tiempo de ejecución
    def builder(self, builder: PizzaBuilder):
        self._builder = builder

    def crear_pizza(self):
        self.builder.añadir_masa()
        self.builder.añadir_salsa()
        self.builder.añadir_ingredientes_principales()
        self.builder.añadir_coccion()
        self.builder.añadir_presentacion()
        self.builder.añadir_maridaje_recomendado()
        self.builder.añadir_extra()

    def get_pizza(self):
        return self.builder.pizza
```

```
from pizza_director import PizzaDirector
from personalizarpizza import PizzaCustomizadaBuilder
from validar import PizzaValidator
from crearCVS import PizzaCSV



#-----------------------------------------
#Client
#-----------------------------------------

if __name__ == "__main__":
    director = PizzaDirector()
    director.builder = PizzaCustomizadaBuilder()
    csv_writer = PizzaCSV("pizzas.csv")  

    while True:
        director.crear_pizza()
        pizza = director.get_pizza()

        validator = PizzaValidator(director.builder)
        validator.set_pizza(pizza)

        while True:
            if validator.verificar_pizza():
                # Escribe la fila de datos en el archivo CSV
                csv_writer.write_pizza_to_csv(pizza)
                break  # Sal del bucle interno después de confirmar

        break  # Sal del bucle principal después de confirmar


```

Además creamos otra función que servirá para guardar el CSV:

```
import csv
#-----------------------------------------
#Creamos un CSV donde almacenar las elecciones de los clientes
#-----------------------------------------

class PizzaCSV:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_pizza_to_csv(self, pizza):
        with open(self.file_name, mode='a', newline='') as file:
            fieldnames = ['Masa', 'Salsa', 'Ingredientes Principales', 'Cocción', 'Presentación', 'Maridaje', 'Extras']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            #Si el archivo está vacío o no existe, escribe la fila de encabezado
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'Masa': pizza.masa,
                'Salsa': pizza.salsa,
                'Ingredientes Principales': ', '.join(pizza.ingredientes_principales),
                'Cocción': pizza.coccion,
                'Presentación': pizza.presentacion,
                'Maridaje': pizza.maridaje_recomendado,
                'Extras': pizza.extra
            })

```
Tambien creamos una clase que sera quien nos muestre las elecciones y nos permita confirmar o modificar

```
from pizza_builder import PizzaBuilder
from pizza import Pizza
from pizza_director import PizzaDirector
from personalizarpizza import PizzaCustomizadaBuilder


#-----------------------------------------
#Creamos una clase que muestre la pizza, por si se necesita modificar
#-----------------------------------------
class PizzaValidator:
    def __init__(self, builder):
        self.builder = builder
        self.pizza = None

    def set_pizza(self, pizza):
        self.pizza = pizza

    def mostrar_resumen(self):
        if self.pizza:
            print("Resumen de selecciones:")
            print(f"Masa: {self.pizza.masa}")
            print(f"Salsa: {self.pizza.salsa}")
            print(f"Ingredientes Principales: {', '.join(self.pizza.ingredientes_principales)}")
            print(f"Cocción: {self.pizza.coccion}")
            print(f"Presentación: {self.pizza.presentacion}")
            print(f"Maridaje: {self.pizza.maridaje_recomendado}")
            print(f"Extras: {self.pizza.extra}")
        else:
            print("No hay una pizza configurada para mostrar un resumen.")

    def verificar_pizza(self):
        self.mostrar_resumen()
        if self.pizza:
            print("¿Estás satisfecho con las modificaciones realizadas en la pizza?")
            confirmacion = input('Responde "si" para confirmar la pizza o "no" para seguir modificando: ')
            if confirmacion.lower() == 'si':
                print("Pizza confirmada. ¡Gracias por tu pedido!")
                return True
            elif confirmacion.lower() == 'no':
                self.modificar_selecciones()
                return self.verificar_pizza()
            else:
                print("Respuesta no válida. Debes responder 'si' o 'no.")
                return self.verificar_pizza()
        else:
            print("No hay una pizza configurada para verificar.")

    def modificar_selecciones(self):
        if self.pizza:
            print("Modifica tus selecciones antes de confirmar:")
            self.builder = PizzaCustomizadaBuilder()
            director = PizzaDirector()
            director.builder = self.builder
            director.crear_pizza()
            self.set_pizza(director.get_pizza())
        else:
            print("No hay una pizza configurada para modificar.")

```

Si lo ejecutamos nos saldrá lo siguiente por terminal:

<img width="498" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/2f066dec-0f37-412c-85eb-6967678dbddf">
<img width="503" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/badc084e-f3e2-40ca-8305-76c5721135ed">
<img width="504" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/2948af66-45b9-4339-bdd1-f1203f0d1cbb">
<img width="358" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/ffd18f67-1975-4ae1-ad70-27fa0072ec68">
<img width="500" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/487887c0-6b8d-4c5d-a855-7324f9bba302">
<img width="501" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/410c3280-36c2-4628-b92b-e0e5b69c4fab">


como vemos nos hace recomendaciones

<img width="362" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/1a713651-214d-4c9f-a504-edce41a015cf">
<img width="496" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/3d9d1b48-10e4-4b4a-a03a-0a6ef5495953">
<img width="498" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/354fb21f-9c4f-4ce6-95bd-c28115be814e">


Luego nos muestra un resumen de nuestro pedido y nos pide si estamos satisfechos
<img width="441" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/488499c2-a353-4e1a-bde0-43134616b50e">
<img width="498" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/730e9860-ddbb-4494-8005-f4ff1b47e15a">
<img width="318" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/aed6315e-c2ca-4304-9813-685fc62bda2d">


***

## Página web:<a name="id3"></a>

A continuación mostraremos la pagina web: (***PARA EJECUTARLA EN TERMINAL HAY QUE PONER python manage.py runserver, TAMBIEN INSTALAR EL DJANGO CON pip install django y TAMBIEN HAY QUE INSTALAR LO SIGUIENTE: pip install crispy_bootstrap4 y python -m pip install django-crispy-forms, SI FUERA NECESARIO TAMBIEN PODRIAS PONER python -m pip install --upgrade pip)

<img width="1436" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/4a6b782c-e75a-4f80-9b4b-389a30a23784">

<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/1abf9749-ed61-4271-b2aa-2693041aa15d">


Como vemos la página web cuenta con la posibilidad de poder registrarse o iniciar sesión:

<img width="182" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/6325f850-30e1-4f01-931f-ceba90f81ae6">


Si pinchamos en registrarse veremos lo siguiente:

<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/79cb7b63-1d5d-428b-afc2-b32b7af75aa7">


Si nos registramos veremos lo siguiente:

<img width="302" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/c4867435-7910-4c4d-9088-5e4f27c13d5e">


Como vemos podemos cerrar sesión y entonces como ya nos hemos registrado ya si podemos darle a iniciar sesión:

<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/3f25f3ac-2206-47c2-9737-2e205ab64459">


En el caso de meter mal algunos datos por ejemplo en la parte de iniciar sesión veriamos como se nos muestra el error:

<img width="1146" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/79e4cee5-8ad2-4dc2-b99a-8b201c2d7ee6">


Esto también pasa en el apartado de registrarse si no se cumplen los requisitos:

<img width="1164" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/752d2a56-92c6-454d-badf-f81e58f93fd4">


Los datos se guardan en un archivo SQL donde la contraseña se encripta para mayor seguridad:

<img width="580" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/65177715-03cd-40dd-a6ae-655ee42f91bd">


Una vez dentro de la página puede pedir una pizza:

<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/875f7632-5ffd-4f3d-8dd5-993461fbed53">


Una vez seleccionado te muestra un resumen y te dice si quieres modificar o confirmar:

<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/7636b21b-7c48-4bd8-b92f-0ef5264c747e">


Y todo esto se guarda en un CSV:
<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/55c4c4c9-0911-42ce-a42c-2fa592b8f6ad">

<img width="1440" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/971d62cd-f509-495c-aaab-363b7e0b21f2">



***

## ¿Por qué el patrón Builder?:<a name="id4"></a>

# Delizioso Pizza Personalization Platform

## Uso del Patrón Builder

El uso del patrón Builder en este escenario de diseño para la plataforma de personalización de pizzas de "Delizioso" es una elección acertada debido a la complejidad y variabilidad de las opciones disponibles. A continuación, se justifica el uso del patrón Builder y se explica cómo contribuye a la robustez y adaptabilidad del sistema:

### Complejidad en la construcción de objetos:

**Justificación:** La creación de pizzas personalizadas implica la combinación de numerosos elementos, desde el tipo de masa hasta los ingredientes y la presentación. Utilizar un constructor (Builder) ayuda a manejar esta complejidad al dividir la construcción del objeto final (pizza) en pasos individuales.

### Validación de elecciones previas del cliente:

**Justificación:** El patrón Builder permite la validación de cada elección en el momento en que se realiza, asegurando que cada componente sea compatible con las selecciones previas del cliente. Esto garantiza una experiencia de usuario coherente y evita combinaciones no deseadas o inválidas.

### Sistema de recomendaciones:

**Justificación:** Al utilizar el patrón Builder, se puede integrar fácilmente un sistema de recomendaciones en cada paso de la construcción. Cada componente del Builder puede tener su propio conjunto de recomendaciones basadas en las elecciones previas del cliente, proporcionando sugerencias personalizadas y mejorando la experiencia del usuario.

### Almacenamiento en un archivo CSV:

**Justificación:** El patrón Builder permite controlar y registrar cada detalle de la construcción de la pizza. Al utilizar un builder, es sencillo capturar y almacenar la información en un formato estructurado como un archivo CSV. Esto facilita el análisis posterior, las recomendaciones personalizadas y el marketing dirigido.

### Reconstrucción y edición desde el archivo CSV:

**Justificación:** La capacidad de reconstruir una pizza a partir de un archivo CSV se simplifica con el patrón Builder. Cada paso de la construcción se puede leer y aplicar para recrear la pizza de manera precisa, permitiendo a los clientes visualizar, editar o reordenar sus creaciones anteriores de manera eficiente.

### Flexibilidad y mantenibilidad del sistema:

**Justificación:** El patrón Builder ofrece flexibilidad al permitir la incorporación de nuevos componentes o la modificación de existentes sin afectar el resto del sistema. Esto es crucial para una pizzería que está constantemente innovando y agregando nuevas opciones a su menú.

### Interfaz de usuario amigable:

**Justificación:** El patrón Builder facilita la creación de una interfaz de usuario amigable guiando al cliente paso a paso. Cada paso del Builder puede mostrar información relevante sobre las opciones disponibles, facilitando la toma de decisiones del cliente.

### Medidas de seguridad:

**Justificación:** El patrón Builder permite implementar medidas de seguridad en cada paso de la construcción, asegurando la integridad de los datos almacenados y la privacidad de las elecciones de los clientes. Se pueden incorporar validaciones y controles de acceso de manera efectiva.

En resumen, el uso del patrón Builder en este escenario ofrece una forma estructurada y eficiente de manejar la complejidad de la personalización de pizzas, garantizando robustez, adaptabilidad y una experiencia de usuario optimizada. La modularidad inherente al patrón Builder facilita la expansión y mantenimiento del sistema a medida que la pizzería evoluciona.


***


<h4>Resumen</h4>


## Uso del Patrón Builder

El patrón Builder se utiliza en este proyecto para construir objetos paso a paso, permitiendo aplazar pasos de la construcción o ejecutarlos de forma recursiva. Esto facilita la creación de representaciones personalizadas de productos, como pizzas.

### Principales beneficios del Patrón Builder:

- **Reutilización de código:** Permite reutilizar el mismo código de construcción para crear varias representaciones de productos, mejorando la eficiencia del desarrollo.

- **Principio de responsabilidad única:** Aísla un código de construcción complejo de la lógica de negocio del producto, mejorando la mantenibilidad y la claridad del código.

Este enfoque estructurado ofrece flexibilidad y adaptabilidad al sistema de personalización de pizzas de "Delizioso", garantizando una experiencia de usuario optimizada y facilitando futuras expansiones y modificaciones del sistema.


## Ejercicio 3:<a name="id5"></a>



















