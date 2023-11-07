from abc import ABC, abstractmethod
import csv

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

            
#-----------------------------------------
#Client
#-----------------------------------------

if __name__ == "__main__":
    
    director = PizzaDirector()
    director.builder = PizzaCustomizadaBuilder()

    while True:
        director.crear_pizza()
        pizza = director.get_pizza()

        csv_writer = PizzaCSV("pizzas.csv")
        validator = PizzaValidator(director.builder)
        validator.set_pizza(pizza)

        while True:
            if validator.verificar_pizza():
                break  # Sal del bucle interno después de confirmar

        break  # Sal del bucle principal después de confirmar










