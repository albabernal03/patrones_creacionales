from graficas import Graficas


#ConcreteProductB2 

class GraficaPastel(Graficas):
    def grafica(self) -> None:
        # Leer el archivo CSV utilizando pandas
        df = pd.read_csv('emergencias.csv')
        
        # Mostrar las opciones disponibles al usuario
        print("Opciones disponibles:")
        print("1. FECHA_NUM")
        print("2. ID-EVENTO")
        
        # Solicitar al usuario que ingrese el número de la opción deseada
        opcion = int(input("Ingrese el número de la opción que desea utilizar: "))
        
        # Verificar si la opción ingresada por el usuario es válida
        if opcion == 1:
            columna_seleccionada = 'FECHA_NUM'
        elif opcion == 2:
            columna_seleccionada = 'ID-EVENTO'
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
            return
        
        # Crear la gráfica de pastel utilizando la columna seleccionada
        df[columna_seleccionada].value_counts().plot(kind='pie', autopct='%0.1f %%')
        
        # Mostrar la gráfica
        plt.show()

