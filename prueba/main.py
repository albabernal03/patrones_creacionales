from calculosfecha_factory import Calculos_estadistico_fecha
from graficasfecha_factory import CrearGrafica_fecha
from elegircal import MMM
from caculosfecha_provider import Calculosfechaprovider

#Client

def main():
    elegircal= MMM.MEDIA


    factory = calculosfecha_provider.create_calculos(elegircal)
    calcular_media= factory.crear_calculos()
 
    
    print(f'media: {calcular_media.calcular()}')

    factory2= CrearGrafica_fecha()
    grafica= factory2.crear_graficas()

    print(f'grafica: {grafica.grafica()}')


if __name__ == "__main__":
    main()
