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


<h3>Ejercicio 4:</h3>


La tarea consiste en abordar los desafíos de gestionar una gran cantidad de documentos digitales en el contexto del SAMUR-Protección Civil después de su proceso de digitalización. Esto implica la creación de un sistema que maneje documentos, enlaces y carpetas, con la necesidad de garantizar un acceso rápido pero seguro, especialmente para datos sensibles. Para lograr esto, se propone el uso de dos patrones de diseño: Composite, para modelar la estructura de documentos del sistema, y Proxy, para controlar y registrar el acceso a documentos específicos. La implementación se llevará a cabo en Python, incorporando buenas prácticas de programación. Además, se deben crear funciones que faciliten la navegación, creación, modificación y eliminación de elementos en el sistema, y se deben realizar pruebas para asegurar la correcta implementación, prestando especial atención a la seguridad y al registro de acceso a los documentos.
***
<h2>Indice</h2>

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Implementacion del ejercicio 2 en una página web](#id3)
4. [¿Por qué usamos elpatrón Builder?](#id4)
5. [Ejercicio 3](#id5)
6. [Implementacion ejercicio 3 en una página web](#id6)
7. [Ejercicio 4](#id7)

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


<h3>Resumen</h3>


## Uso del Patrón Builder

El patrón Builder se utiliza en este proyecto para construir objetos paso a paso, permitiendo aplazar pasos de la construcción o ejecutarlos de forma recursiva. Esto facilita la creación de representaciones personalizadas de productos, como pizzas.

### Principales beneficios del Patrón Builder:

- **Reutilización de código:** Permite reutilizar el mismo código de construcción para crear varias representaciones de productos, mejorando la eficiencia del desarrollo.

- **Principio de responsabilidad única:** Aísla un código de construcción complejo de la lógica de negocio del producto, mejorando la mantenibilidad y la claridad del código.

Este enfoque estructurado ofrece flexibilidad y adaptabilidad al sistema de personalización de pizzas de "Delizioso", garantizando una experiencia de usuario optimizada y facilitando futuras expansiones y modificaciones del sistema.


## Ejercicio 3:<a name="id5"></a>

```
from abc import ABC, abstractmethod


#------------------------------------------------------------
# Component
#------------------------------------------------------------

class ComponentMenu(ABC):
    '''La clase Componente base define operaciones comunes para objetos de composición,
    ya sean simples o complejos'''

    @abstractmethod
    def mostrar(self):
        pass

```

```

#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Pizza(ComponentMenu):

    '''La clase Hoja representa los elementos finales en una composición. Una hoja no tiene elementos adicionales.
    En general, son las hojas las que realizan el trabajo real, mientras que los objetos Compuesto solo delegan 
    en sus partes internas.'''

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


    def mostrar(self):
        print(f'Pizza: {self.nombre} - Precio: {self.precio}')

```
```
#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Bebida(ComponentMenu):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.precio}')
```
```
#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Entrante(ComponentMenu):
        
            def __init__(self, nombre, precio):
                self.nombre = nombre
                self.precio = precio
        
            def mostrar(self):
                print(f'Entrante: {self.nombre} - Precio: {self.precio}')



```
```
#------------------------------------------------------------
# Leaf
#------------------------------------------------------------

class Postre(ComponentMenu):
    
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
    
        def mostrar(self):
            print(f'Postre: {self.nombre} - Precio: {self.precio}')

```
```
#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class Combo(ComponentMenu):

    '''
    La clase Compuesto representa los componentes complejos que pueden tener hijos. Por lo general, 
    los objetos Compuesto delegan el trabajo real a sus hijos y luego "resumen" el resultado.
    '''

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)
    
    def mostrar(self):
        print(f'Combo: {self.nombre}')

        for elemento in self.elementos:
            elemento.mostrar()

        print(f'Precio Total del Combo: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        return sum(elemento.precio for elemento in self.elementos)

```

```
#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class ComboPareja(ComponentMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.combo1 = None
        self.combo2 = None

    def personalizar(self, combo1, combo2):
        self.combo1 = combo1
        self.combo2 = combo2

    def mostrar(self):
        print(f'Combo Pareja: {self.nombre}')
        if self.combo1:
            print(f'Menu:')
            self.combo1.mostrar()
        if self.combo2:
            print(f'Menu:')
            self.combo2.mostrar()
        print(f'Precio Total del Combo Pareja: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        total_combo1 = self.combo1.calcular_precio_total() if self.combo1 else 0
        total_combo2 = self.combo2.calcular_precio_total() if self.combo2 else 0
        return total_combo1 + total_combo2
    
```
```
#------------------------------------------------------------
# CSV
#------------------------------------------------------------


def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    with open(nombre_archivo, 'a') as archivo:
        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            for subelemento in elemento.elementos:
                guardar_elemento_csv(subelemento, nombre_archivo, usuario)
        elif isinstance(elemento, ComboPareja):
            archivo.write(f'{usuario},ComboPareja,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            if elemento.combo1:
                guardar_elemento_csv(elemento.combo1, nombre_archivo, usuario)
            if elemento.combo2:
                guardar_elemento_csv(elemento.combo2, nombre_archivo, usuario)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            archivo.write(f'{usuario},{type(elemento).__name__},{elemento.nombre},{elemento.precio}\n')

def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    with open(nombre_archivo, 'a') as archivo:
        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            for subelemento in elemento.elementos:
                guardar_elemento_csv(subelemento, nombre_archivo, usuario)
        elif isinstance(elemento, ComboPareja):
            archivo.write(f'{usuario},ComboPareja,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            if elemento.combo1:
                guardar_elemento_csv(elemento.combo1, nombre_archivo, usuario)
            if elemento.combo2:
                guardar_elemento_csv(elemento.combo2, nombre_archivo, usuario)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            archivo.write(f'{usuario},{type(elemento).__name__},{elemento.nombre},{elemento.precio}\n')

def leer_elementos_csv(nombre_archivo, usuario):
    elementos = []
    combos = {}

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            usuario_archivo, tipo_elemento, nombre_elemento, precio_elemento = linea.strip().split(',')
            if usuario_archivo == usuario:
                if tipo_elemento == 'Combo':
                    combo = Combo(nombre_elemento)
                    combos[nombre_elemento] = combo
                    elementos.append(combo)
                elif tipo_elemento == 'ComboPareja':
                    combo_pareja = ComboPareja(nombre_elemento)
                    combo_pareja.combo1 = combos.get(nombre_elemento + "_1")
                    combo_pareja.combo2 = combos.get(nombre_elemento + "_2")
                    elementos.append(combo_pareja)
                elif tipo_elemento in ['Pizza', 'Bebida', 'Entrante', 'Postre']:
                    clase_elemento = globals()[tipo_elemento]
                    elemento = clase_elemento(nombre_elemento, float(precio_elemento))
                    elementos.append(elemento)

    return elementos




def preguntar_guardar_historial():
    while True:
        respuesta = input("¿Deseas guardar el historial de pedidos? (s/n): ").lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

def reconstruir_menu_desde_historial(nombre_archivo, usuario):
    elementos = leer_elementos_csv(nombre_archivo, usuario)
    menu_reconstruido = []

    for elemento in elementos:
        if isinstance(elemento, Combo):
            combo_reconstruido = Combo(elemento.nombre)
            for subelemento in elemento.elementos:
                subelemento_reconstruido = reconstruir_elemento_desde_historial(subelemento, elementos)
                combo_reconstruido.agregar_elemento(subelemento_reconstruido)
            menu_reconstruido.append(combo_reconstruido)
        elif isinstance(elemento, ComboPareja):
            combo_pareja_reconstruido = ComboPareja(elemento.nombre)
            combo_pareja_reconstruido.combo1 = reconstruir_elemento_desde_historial(elemento.combo1, elementos)
            combo_pareja_reconstruido.combo2 = reconstruir_elemento_desde_historial(elemento.combo2, elementos)
            menu_reconstruido.append(combo_pareja_reconstruido)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            elemento_reconstruido = reconstruir_elemento_desde_historial(elemento, elementos)
            menu_reconstruido.append(elemento_reconstruido)

    return menu_reconstruido


def reconstruir_elemento_desde_historial(elemento, elementos):
    if isinstance(elemento, Combo):
        combo_reconstruido = Combo(elemento.nombre)
        for subelemento in elemento.elementos:
            subelemento_reconstruido = reconstruir_elemento_desde_historial(subelemento, elementos)
            combo_reconstruido.agregar_elemento(subelemento_reconstruido)
        return combo_reconstruido
    elif isinstance(elemento, ComboPareja):
        combo_pareja_reconstruido = ComboPareja(elemento.nombre)
        combo_pareja_reconstruido.combo1 = reconstruir_elemento_desde_historial(elemento.combo1, elementos)
        combo_pareja_reconstruido.combo2 = reconstruir_elemento_desde_historial(elemento.combo2, elementos)
        return combo_pareja_reconstruido
    elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
        return elemento

```
```
#------------------------------------------------------------
# Main
#------------------------------------------------------------

def solicitar_opcion(mensaje, opciones):
    while True:
        try:
            eleccion = int(input(mensaje))
            if eleccion in opciones:
                return eleccion
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
        except ValueError:
            print("Error: Ingresa un número entero.")


if __name__ == "__main__":
    # Solicitar al usuario que ingrese su nombre
    usuario = input("Introduce tu nombre de usuario: ")
    pedidos_usuario = leer_elementos_csv('pedidos.csv', usuario)

     # Crear instancias de elementos individuales (pizzas, bebidas, entrantes, postres)
    pizza_margarita = Pizza("Margarita", 10.0)
    pizza_pepperoni = Pizza("Pepperoni", 12.0)
    pizza_vegetariana = Pizza("Vegetariana", 11.0)
    pizza_hawaiana = Pizza("Hawaiana", 13.0)
    pizza_cuatros_quesos = Pizza("Cuatro Quesos", 14.0)

    bebida_cola = Bebida("Coca-Cola", 2.0)
    bebida_agua = Bebida("Agua", 1.5)
    bebida_fanta_de_naranja = Bebida("Fanta de Naranja", 2.0)
    bebida_cerveza = Bebida("Cerveza", 3.5)
    bebida_nestea=Bebida("Nestea", 2.0)

    entrante_ensalada = Entrante("Ensalada", 5.0)
    entrante_patatas = Entrante("Patatas", 4.0)
    entrante_alitas = Entrante("Alitas de Pollo", 6.0)
    entrante_nuggets = Entrante("Nuggets", 5.0)
    entrante_nachos = Entrante("Nachos", 5.0)

    postre_tarta_de_queso= Postre("Tarta de queso", 6.0)
    postre_helado = Postre("Helado", 3.0)
    postre_frutas = Postre("Frutas", 4.0)
    postre_natillas = Postre("Natillas", 3.0)
    postre_tarta_de_la_abuela = Postre("Tarta de la abuela", 5.0)


    # Crear combos predefinidos
    combo_1 = Combo("Combo 1")
    combo_1.agregar(entrante_ensalada)
    combo_1.agregar(pizza_margarita)
    combo_1.agregar(bebida_cola)
    combo_1.agregar(postre_helado)

    combo_2 = Combo("Combo 2")
    combo_2.agregar(entrante_patatas)
    combo_2.agregar(pizza_pepperoni)
    combo_2.agregar(bebida_agua)
    combo_2.agregar(postre_frutas)

    combo_3 = Combo("Combo 3")
    combo_3.agregar(entrante_alitas)
    combo_3.agregar(pizza_vegetariana)
    combo_3.agregar(bebida_fanta_de_naranja)
    combo_3.agregar(postre_natillas)

    combo_4 = Combo("Combo 4")
    combo_4.agregar(entrante_nuggets)
    combo_4.agregar(pizza_hawaiana)
    combo_4.agregar(bebida_cerveza)
    combo_4.agregar(postre_tarta_de_la_abuela)

  # Crear combos pareja predefinidos

    combo_pareja_1 = ComboPareja("Combo Pareja 1")
    combo_pareja_1.personalizar(combo_1, combo_2)

    combo_pareja_2 = ComboPareja("Combo Pareja 2")
    combo_pareja_2.personalizar(combo_3, combo_4)





    # Mostrar combos predefinidos
    while True:
        print("\nCombos predefinidos:")
        combo_1.mostrar()
        combo_2.mostrar()
        combo_3.mostrar()
        combo_4.mostrar()
        print("\nCombos Pareja predefinidos:")
        combo_pareja_1.mostrar()
        combo_pareja_2.mostrar()

        print("\nOpciones:")
        print("1. Crear combo personalizado")
        print("2. Elegir combo predefinido")
        print('3. Elegir combo pareja predefinido')
        print('4.Mostrar historial de pedidos')
        print('5. Reconstruir menú desde historial')
        eleccion = solicitar_opcion("Elige una opción (1, 2, 3, 4, 5 o 6): ", [1, 2, 3, 4, 5, 6])

        if eleccion == 1:
            # Solicitar al usuario que elija elementos para el combo personalizado
            print("\nElige los elementos para tu combo personalizado:")
            eleccion_entrante = solicitar_opcion(
                "\nOpciones de entrantes:\n1. Ensalada\n2. Patatas\n3. Alitas de Pollo\n4. Nuggets\n5. Nachos\nElige un entrante (1, 2, 3, 4 o 5): ",
                [1, 2, 3, 4, 5]
            )
            eleccion_pizza = solicitar_opcion(
                "\nOpciones de pizzas:\n1. Margarita\n2. Pepperoni\n3. Vegetariana\n4. Hawaiana\n5. Cuatro Quesos\nElige una pizza (1, 2, 3, 4 o 5): ",
                [1, 2, 3, 4, 5]
            )
            eleccion_bebida = solicitar_opcion(
                "\nOpciones de bebidas:\n1. Cola\n2. Agua\n3. Fanta de Naranja\n4. Cerveza\n5. Nestea\nElige una bebida (1, 2, 3, 4 o 5): ",
                [1, 2, 3, 4, 5]
            )
            eleccion_postre = solicitar_opcion(
                "\nOpciones de postres:\n1. Tarta de queso\n2. Helado\n3. Frutas\n4. Natillas\n5. Tarta de la abuela\nElige un postre (1, 2, 3, 4 o 5): ",
                [1, 2, 3, 4, 5]
            )

            # Crear el combo personalizado
            combo_personalizado = Combo("Combo Personalizado")
            # Agregar elementos al combo personalizado según las elecciones del usuario
            if eleccion_entrante == 1:
                combo_personalizado.agregar(entrante_ensalada)
            elif eleccion_entrante == 2:
                combo_personalizado.agregar(entrante_patatas)
            elif eleccion_entrante == 3:
                combo_personalizado.agregar(entrante_alitas)
            elif eleccion_entrante == 4:
                combo_personalizado.agregar(entrante_nuggets)
            elif eleccion_entrante == 5:
                combo_personalizado.agregar(entrante_nachos)

            if eleccion_pizza == 1:
                combo_personalizado.agregar(pizza_margarita)
            elif eleccion_pizza == 2:
                combo_personalizado.agregar(pizza_pepperoni)
            elif eleccion_pizza == 3:
                combo_personalizado.agregar(pizza_vegetariana)
            elif eleccion_pizza == 4:
                combo_personalizado.agregar(pizza_hawaiana)
            elif eleccion_pizza == 5:
                combo_personalizado.agregar(pizza_cuatros_quesos)

            if eleccion_bebida == 1:
                combo_personalizado.agregar(bebida_cola)
            elif eleccion_bebida == 2:
                combo_personalizado.agregar(bebida_agua)
            elif eleccion_bebida == 3:
                combo_personalizado.agregar(bebida_fanta_de_naranja)
            elif eleccion_bebida == 4:
                combo_personalizado.agregar(bebida_cerveza)
            elif eleccion_bebida == 5:
                combo_personalizado.agregar(bebida_nestea)

            if eleccion_postre == 1:
                combo_personalizado.agregar(postre_tarta_de_queso)
            elif eleccion_postre == 2:
                combo_personalizado.agregar(postre_helado)
            elif eleccion_postre == 3:
                combo_personalizado.agregar(postre_frutas)
            elif eleccion_postre == 4:
                combo_personalizado.agregar(postre_natillas)
            elif eleccion_postre == 5:
                combo_personalizado.agregar(postre_tarta_de_la_abuela)

            # Mostrar el combo personalizado
            print("\nTu combo personalizado:")
            combo_personalizado.mostrar()
            #preguntamos si quiere guardar el historial
            if preguntar_guardar_historial():
                guardar_elemento_csv(combo_personalizado, 'pedidos.csv', usuario)
            else:
                print("No se guardará el historial de pedidos.")

        elif eleccion == 2:
            # Solicitar al usuario que elija un combo predefinido y mostrarlo
            opciones_combos_predefinidos = [1, 2, 3]
            eleccion_combo_predefinido = solicitar_opcion("Elige un combo predefinido (1, 2 o 3): ", opciones_combos_predefinidos)

            chosen_combo = None

            if eleccion_combo_predefinido == 1:
                chosen_combo = combo_1
            elif eleccion_combo_predefinido == 2:
                chosen_combo = combo_2
            elif eleccion_combo_predefinido == 3:
                chosen_combo = combo_3

            # Mostrar el combo predefinido
            print("\nEl combo predefinido que has elegido es:")
            chosen_combo.mostrar()

            # Preguntar si quieren pedir este combo
            if input("¿Quieres pedir este combo? (s/n): ").lower() == 's':
                if preguntar_guardar_historial():
                    guardar_elemento_csv(chosen_combo, 'pedidos.csv', usuario)
                else:
                    print("No se guardará el historial de pedidos.")
            else:
                print("Pedido cancelado.")

        elif eleccion == 3:
            combo_pareja_personalizado = ComboPareja("Combo Pareja Personalizado")

            print("\nElige los combos para tu Combo Pareja:")
            print("1. Combo 1")
            print("2. Combo 2")
            eleccion_combo1 = solicitar_opcion("Elige el Combo 1 (1 o 2): ", [1, 2])
            eleccion_combo2 = solicitar_opcion("Elige el Combo 2 (1 o 2): ", [1, 2])

            if eleccion_combo1 == 1:
                combo_pareja_personalizado.personalizar(combo_1, None)
            elif eleccion_combo1 == 2:
                combo_pareja_personalizado.personalizar(combo_2, None)

            if eleccion_combo2 == 1:
                combo_pareja_personalizado.personalizar(combo_pareja_personalizado.combo1, combo_1)
            elif eleccion_combo2 == 2:
                combo_pareja_personalizado.personalizar(combo_pareja_personalizado.combo1, combo_2)

            # Mostrar el Combo Pareja personalizado
            print("\nTu Combo Pareja personalizado:")
            combo_pareja_personalizado.mostrar()
            #preguntamos si quiere guardar el historial
            if preguntar_guardar_historial():
                guardar_elemento_csv(combo_pareja_personalizado, 'pedidos.csv', usuario)
            else:
                print("No se guardará el historial de pedidos.")

        elif eleccion == 4:
    # Mostrar historial de pedidos según usuario
            print("\nHistorial de pedidos:")
            pedidos_usuario = leer_elementos_csv('pedidos.csv', usuario)

            if pedidos_usuario:
                print(f"\nPedidos antiguos de {usuario}:")
                for pedido in pedidos_usuario:
                    if isinstance(pedido, Combo):
                        print("\nPedido Combo:")
                        pedido.mostrar()
                    elif isinstance(pedido, ComboPareja):
                        print("\nPedido Combo Pareja:")
                        pedido.mostrar()
                    else:
                        print(f'{type(pedido).__name__}: {pedido.nombre} - Precio: {pedido.precio}')
            else:
                print(f"No hay pedidos antiguos de {usuario}.")


        elif eleccion == 5:
            # Reconstruir menú desde historial
            menu_reconstruido = reconstruir_menu_desde_historial('pedidos.csv', usuario)
            if menu_reconstruido:
                print("\nMenú reconstruido desde historial:")
                for item in menu_reconstruido:
                    if isinstance(item, Combo):
                        print("\nCombo:")
                        item.mostrar()
                    elif isinstance(item, ComboPareja):
                        print("\nCombo Pareja:")
                        item.mostrar()
                    else:
                        print(f'{type(item).__name__}: {item.nombre} - Precio: {item.precio}')
            else:
                print("No hay historial de pedidos para reconstruir el menú.")

        elif eleccion == 6:
            # Salir del programa
            print("Saliendo del programa...")
```
***

<h3>Diagrama UML</h3>

<img width="783" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/0bcf1ac4-dcbc-4c87-91c4-c62a08ca1da8">

***

<h3>Justificación</h3>

Este código implementa un patrón de diseño estructural llamado "Composite". El patrón Composite se utiliza para tratar tanto a los objetos individuales como a las composiciones de objetos de manera uniforme. En este caso, los elementos del menú (como pizzas, bebidas, etc.) se representan mediante una interfaz común llamada ComponentMenu, que tiene un método mostrar.

Aquí hay algunas decisiones de diseño notables y la aplicación del patrón Composite:

1.**Interfaz Abstracta (ComponentMenu):**

Se ha definido una interfaz abstracta llamada ComponentMenu que declara el método mostrar. Esta interfaz es la base tanto para los elementos individuales (Pizza, Bebida, etc.) como para las composiciones (Combo, ComboPareja).

2.**Elementos Individuales (Leafs):**

Las clases Pizza, Bebida, Entrante y Postre implementan la interfaz ComponentMenu. Estas son las hojas del árbol de composición y representan elementos individuales del menú.

3.**Composiciones (Composite):**

Las clases Combo y ComboPareja implementan la interfaz ComponentMenu y actúan como contenedores para elementos individuales o sub-combos. Estos son los nodos compuestos que pueden contener hojas o sub-combos.

4.**Método Recursivo mostrar:**

El método mostrar se implementa de manera recursiva en las clases Combo y ComboPareja. Esto permite que un combo muestre su contenido, ya sean elementos individuales o sub-combos.

5.**Patrón Composite en Acción:**

Se utiliza el patrón Composite al tratar a los elementos del menú de manera uniforme a través de la interfaz común ComponentMenu. Esto simplifica el código del cliente, ya que puede interactuar con elementos individuales y composiciones de manera consistente.

6.**Persistencia en CSV:**

Se proporcionan funciones para guardar y leer elementos del menú en un archivo CSV. Esto permite almacenar y recuperar historiales de pedidos para usuarios específicos.

7.**Menús Predefinidos y Personalizados:**

Se han creado combos y combos pareja predefinidos (combo_1, combo_2, combo_pareja_1, etc.). También se permite al usuario crear su propio combo personalizado.

8.**Historial de Pedidos:**

Se ofrece la opción de guardar el historial de pedidos en un archivo CSV. El historial se puede mostrar posteriormente para un usuario específico.

En resumen, este código demuestra un buen uso del patrón Composite para modelar elementos del menú y combos, proporcionando una interfaz consistente para interactuar con elementos individuales y composiciones. La persistencia en CSV y la capacidad de crear combos personalizados añaden funcionalidad adicional al programa.


***

<h3>Pruebas unitarias</h3>

```
import unittest
from unittest.mock import patch
from io import StringIO
from main import *

class TestMenu(unittest.TestCase):

    def setUp(self):
        # Crear instancias de elementos individuales
        self.pizza_margarita = Pizza("Margarita", 10.0)
        self.bebida_cola = Bebida("Coca-Cola", 2.0)
        self.entrante_ensalada = Entrante("Ensalada", 5.0)

        # Crear combos predefinidos
        self.combo_1 = Combo("Combo 1")
        self.combo_1.agregar(self.entrante_ensalada)
        self.combo_1.agregar(self.pizza_margarita)
        self.combo_1.agregar(self.bebida_cola)

        self.combo_2 = Combo("Combo 2")
        self.combo_2.agregar(self.entrante_ensalada)
        self.combo_2.agregar(self.pizza_margarita)
        self.combo_2.agregar(self.bebida_cola)

        # Crear Combo Pareja predefinido
        self.combo_pareja_1 = ComboPareja("Combo Pareja 1")
        self.combo_pareja_1.personalizar(self.combo_1, self.combo_2)

    def test_pizza_creation(self):
        self.assertEqual(self.pizza_margarita.nombre, "Margarita")
        self.assertEqual(self.pizza_margarita.precio, 10.0)

    def test_bebida_creation(self):
        self.assertEqual(self.bebida_cola.nombre, "Coca-Cola")
        self.assertEqual(self.bebida_cola.precio, 2.0)

    def test_entrante_creation(self):
        self.assertEqual(self.entrante_ensalada.nombre, "Ensalada")
        self.assertEqual(self.entrante_ensalada.precio, 5.0)

    def test_combo_creation(self):
        self.assertEqual(self.combo_1.nombre, "Combo 1")
        self.assertEqual(len(self.combo_1.elementos), 3)

    def test_combo_pareja_creation(self):
        self.assertEqual(self.combo_pareja_1.nombre, "Combo Pareja 1")
        self.assertIsNotNone(self.combo_pareja_1.combo1)
        self.assertIsNotNone(self.combo_pareja_1.combo2)

    @patch("builtins.input", side_effect=["1"])
    def test_solicitar_opcion_valida(self, mock_input):
        opciones = [1, 2, 3]
        eleccion = solicitar_opcion("Elige una opción (1, 2, o 3): ", opciones)
        self.assertEqual(eleccion, 1)

    @patch("builtins.input", side_effect=["4", "3"])
    def test_solicitar_opcion_invalida_then_valida(self, mock_input):
        opciones = [1, 2, 3]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            eleccion = solicitar_opcion("Elige una opción (1, 2, o 3): ", opciones)
            self.assertEqual(eleccion, 3)
            self.assertEqual(mock_stdout.getvalue().strip(), "Opción no válida. Por favor, elige una opción válida.")

    @patch("builtins.input", side_effect=["a", "2"])
    def test_solicitar_opcion_no_entero_then_valida(self, mock_input):
        opciones = [1, 2, 3]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            eleccion = solicitar_opcion("Elige una opción (1, 2, o 3): ", opciones)
            self.assertEqual(eleccion, 2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Error: Ingresa un número entero.")

if __name__ == "__main__":
    unittest.main()

```

## Pagina web:<a name="id6"></a>

Como vemos añadimos una nueva sección a la pizzeria que es para pedir combos

<img width="1353" alt="image" src="https://github.com/albabernal03/patrones_creacionales/assets/91721875/d29f81e7-2391-42cc-9e26-6d46d68b45e5">

Como se ve en la imagen si no iniciamos sesion no se puede hacer el pedido, pues asi cada pedido estará identificado con el usuario




***
## Ejercicio 4:<a name="id7"></a>

```
from abc import ABC, abstractmethod
from datetime import datetime
import json

#------------------------------------------------------------
# Component
#------------------------------------------------------------

class Component(ABC):
    @abstractmethod
    def tamaño(self):
        pass

#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Archivo(Component):
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.tamano = tamano

    def tamaño(self):
        return self.tamano
      
#------------------------------------------------------------
# Composite
#------------------------------------------------------------

class Carpeta(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def tamaño(self):
        total = 0
        for elemento in self.elementos:
            total += elemento.tamaño()
        return total

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)


#------------------------------------------------------------
#Leaf
#------------------------------------------------------------

class Enlace(Component):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.url = destino

    def tamaño(self):
        return 0
    


#------------------------------------------------------------
# Proxy
#------------------------------------------------------------

class ComponentProxy(Component):
    def __init__(self, real_component, access_control=[]):
        self._real_component = real_component
        self._access_control = access_control
        self._access_granted = False
        self._access_log = []

    def tamaño(self):
        if self.check_access():
            return self._real_component.tamaño()
        else:
            return 0

    def check_access(self) -> bool:
        user = input("Introduce el usuario: ")
        if user in self._access_control:
            print(f"Proxy: {user} ha accedido.")
            self._access_granted = True
        else:
            print(f"Proxy: {user} no tiene acceso.")
        return self._access_granted

    def log_access(self) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Se ha accedido: {timestamp}"
        print(f"Proxy: {log_entry}")
        self._access_log.append(log_entry)

    # Forwarding attribute access to the real component
    def __getattr__(self, attr):
        return getattr(self._real_component, attr)


#Funciones para interactuar con la estructura y el Proxy
def navegar(component):
    print(f"El tamaño de {component.nombre} es: {component.tamaño()}")

def agregar(carpeta, elemento):
    carpeta.agregar(elemento)

def modificar_tamano(archivo, nuevo_tamano):
    if isinstance(archivo, Archivo):
        archivo.tamano = nuevo_tamano
        print(f"El tamaño del archivo {archivo.nombre} ha sido modificado a {nuevo_tamano}")
    else:
        print("No se puede modificar el tamaño de una carpeta")

def eliminar(carpeta, elemento):
    carpeta.eliminar(elemento)

def acceder(proxy, usuario):
    proxy.check_access()
    navegar(proxy)  

def revocar_acceso(proxy, usuario):
    proxy._access_granted = False

def encontrar_elemento_por_nombre(component, nombre):
    # Verifica si el componente actual tiene el nombre buscado
    if hasattr(component, 'nombre') and component.nombre == nombre:
        return component

    # Si el componente es una carpeta, busca en sus elementos
    if isinstance(component, Carpeta):
        for elemento in component.elementos:
            resultado = encontrar_elemento_por_nombre(elemento, nombre)
            if resultado:
                return resultado

    # Si no se encuentra en el componente actual ni en sus elementos, retorna None
    return None

# Función para cargar la estructura desde un archivo JSON
def cargar_estructura_desde_json(ruta_archivo):
    print("Attempting to load data from:", ruta_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
        print("Loaded data from JSON:", datos)
        return crear_estructura_desde_json(datos)
    except FileNotFoundError:
        print("File not found:", ruta_archivo)
        return None
    except json.JSONDecodeError as je:
        print("JSON decoding error:", je)
        return None
    except Exception as e:
        print("Error loading data from JSON:", e)
        return None


# Función para crear la estructura desde un diccionario
def crear_estructura_desde_json(datos):
    tipo_componente = datos.get('type')

    if tipo_componente == 'Carpeta':
        carpeta = Carpeta(datos['nombre'])
        for datos_hijo in datos['elementos']:
            componente_hijo = crear_estructura_desde_json(datos_hijo)
            carpeta.agregar(componente_hijo)
        return carpeta

    elif tipo_componente == 'Archivo':
        return Archivo(datos['nombre'], datos['tipo'], datos['tamaño'])

    elif tipo_componente == 'Enlace':
        return Enlace(datos['nombre'], datos['url'])

    else:
        raise ValueError(f"Unknown component type: {tipo_componente}")


# Función recursiva para crear un componente desde un diccionario
def crear_componente_desde_json(datos):
    tipo_componente = datos.get('tipo')
    if tipo_componente == 'Archivo':
        return Archivo(datos['nombre'], datos['tipo'], datos['tamaño'])
    elif tipo_componente == 'Carpeta':
        carpeta = Carpeta(datos['nombre'])
        for datos_hijo in datos['elementos']:
            componente_hijo = crear_componente_desde_json(datos_hijo)
            carpeta.agregar_elemento(componente_hijo)
        return carpeta
    elif tipo_componente == 'Enlace':
        return Enlace(datos['nombre'], datos['url'])

archivo1 = Archivo("Archivo1", "txt", 10)

if __name__ == "__main__":
    # Solicitar al usuario que ingrese su nombre
    usuario = input("Introduce tu nombre de usuario: ")

    # Crear Proxy para el archivo
    proxy_archivo1 = ComponentProxy(archivo1, access_control=['Usuario1', 'Usuario2'])

    # Verificar el acceso del usuario
    if usuario in proxy_archivo1._access_control:
        print(f"Bienvenido, {usuario}.")

        # Cargar la estructura desde un archivo JSON
        structure = cargar_estructura_desde_json('structure.json')

        if structure:
            # Interactuar con la estructura y el Proxy
            navegar(structure)

            # Solicitar al usuario que elija una acción
            accion = input("¿Qué acción deseas realizar? (agregar/modificar/eliminar/nada): ")

            if accion == 'agregar':
                # Solicitar detalles para agregar un nuevo elemento
                tipo_elemento = input("Tipo de elemento (Archivo/Carpeta/Enlace): ")
                nombre_elemento = input("Nombre del elemento: ")

                if tipo_elemento == 'Archivo':
                    tamano_elemento = int(input("Tamaño del archivo: "))
                    nuevo_elemento = Archivo(nombre_elemento, 'tipo_desconocido', tamano_elemento)
                elif tipo_elemento == 'Carpeta':
                    nuevo_elemento = Carpeta(nombre_elemento)
                elif tipo_elemento == 'Enlace':
                    url_elemento = input("URL del enlace: ")
                    nuevo_elemento = Enlace(nombre_elemento, url_elemento)
                else:
                    print("Tipo de elemento desconocido. No se puede agregar.")
                    nuevo_elemento = None

                if nuevo_elemento:
                    agregar(structure, nuevo_elemento)
                    print(f"Elemento {nombre_elemento} agregado.")
                    navegar(structure)

            elif accion == 'modificar':
                # Solicitar detalles para modificar un elemento
                nombre_elemento = input("Nombre del elemento a modificar: ")
                nuevo_tamano = int(input("Nuevo tamaño: "))
                elemento_a_modificar = encontrar_elemento_por_nombre(structure, nombre_elemento)

                if elemento_a_modificar:
                    modificar_tamano(elemento_a_modificar, nuevo_tamano)
                    print(f"Tamaño de {nombre_elemento} modificado.")
                    navegar(structure)
                else:
                    print(f"No se encontró el elemento {nombre_elemento}.")

            elif accion == 'eliminar':
                # Solicitar detalles para eliminar un elemento
                nombre_elemento = input("Nombre del elemento a eliminar: ")
                elemento_a_eliminar = encontrar_elemento_por_nombre(structure, nombre_elemento)

                if elemento_a_eliminar:
                    eliminar(structure, elemento_a_eliminar)
                    print(f"Elemento {nombre_elemento} eliminado.")
                    navegar(structure)
                else:
                    print(f"No se encontró el elemento {nombre_elemento}.")

            elif accion == 'nada':
                print("No se realizarán cambios.")

            else:
                print("Acción no reconocida. No se realizarán cambios.")

        else:
            print("Error loading structure from JSON.")
    else:
        print(f"{usuario}, no tienes acceso a esta estructura.")

```

```
#------------------------------------------------------------
# Json
#------------------------------------------------------------

{
    "type": "Carpeta",
    "nombre": "Raiz",
    "elementos": [
      {
        "type": "Archivo",
        "nombre": "Archivo1",
        "tipo": "txt",
        "tamaño": 10
      },
      {
        "type": "Carpeta",
        "nombre": "Documentos",
        "elementos": [
          {
            "type": "Archivo",
            "nombre": "Informe.pdf",
            "tipo": "pdf",
            "tamaño": 25
          },
          {
            "type": "Carpeta",
            "nombre": "Fotos",
            "elementos": [
              {
                "type": "Archivo",
                "nombre": "Vacaciones.jpg",
                "tipo": "jpg",
                "tamaño": 15
              },
              {
                "type": "Enlace",
                "nombre": "Álbum online",
                "url": "https://album.ejemplo.com"
              }
            ]
          }
        ]
      },
      {
        "type": "Enlace",
        "nombre": "Página principal",
        "url": "https://www.ejemplo.com"
      },
      {
        "type": "Carpeta",
        "nombre": "Proyectos",
        "elementos": [
          {
            "type": "Archivo",
            "nombre": "Proyecto1.docx",
            "tipo": "docx",
            "tamaño": 30
          },
          {
            "type": "Carpeta",
            "nombre": "Código fuente",
            "elementos": [
              {
                "type": "Archivo",
                "nombre": "main.py",
                "tipo": "py",
                "tamaño": 8
              },
              {
                "type": "Archivo",
                "nombre": "utils.py",
                "tipo": "py",
                "tamaño": 5
              }
            ]
          }
        ]
      }
    ]
  }
  

```



















