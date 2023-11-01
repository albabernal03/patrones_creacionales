from calculosfecha_factory import Calculos_estadistico_fecha
from graficas_factory import CrearGrafica

#Client

def main():

    factory = Calculos_estadistico_fecha()
    calcular_media= factory.crear_calculos()
    
    print(f'media: {calcular_media.calcular()}')

    factory2= CrearGrafica()
    grafica= factory2.crear_graficas()

    print(f'grafica: {grafica.grafica()}')


if __name__ == "__main__":
    main()
