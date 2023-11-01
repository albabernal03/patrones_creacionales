from calculos_factory import Calculos_estadistico
from graficas_factory import CrearGrafica

#Client

def main():

    factory = Calculos_estadistico()
    calcular_media= factory.crear_calculos()
    
    print(f'media: {calcular_media.calcular()}')

    factory2= CrearGrafica()
    grafica= factory2.crear_graficas()

    print(f'grafica: {grafica.grafica()}')


if __name__ == "__main__":
    main()
