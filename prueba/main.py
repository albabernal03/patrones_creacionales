from calculosfecha_factory import Calculos_estadistico_fecha
from graficasfecha_factory import CrearGrafica_fecha

#Client

def main():

    factory = Calculos_estadistico_fecha()
    calcular_media= factory.crear_calculos()
 
    
    print(f'media: {calcular_media.calcular()}')
    
    calcular_moda = factory.crear_calculos()  # Crear una nueva instancia para calcular la moda
    print(f'moda: {calcular_moda.calcular()}')

    factory2= CrearGrafica_fecha()
    grafica= factory2.crear_graficas()

    print(f'grafica: {grafica.grafica()}')


if __name__ == "__main__":
    main()
