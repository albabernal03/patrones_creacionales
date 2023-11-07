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


