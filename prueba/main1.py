from calculos_factory import Calculos_estadistico
from graficas_factory import CrearGrafica

#Client

def main():

    factory = Calculos_estadistico()
    calcular_media= factory.crear_calculos()
    
    print(f'media: {calcular_media.calcular()}')


if __name__ == "__main__":
    main()
