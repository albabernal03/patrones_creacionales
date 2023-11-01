from calculos_factory import Calculos_estadistico
from grafica_factory import CrearGrafica

#Client
def main():
    factory=Calculos_estadistico()
    factory.crear_calculos()

    print(f'Calculos:{calculosestadisticos.__class__.__name__}')
    print(f'Media:{calculosestadisticos.media()}')
    print(f'Moda:{calculosestadisticos.moda()}')
    print(f'Mediana:{calculosestadisticos.mediana()}')

if name == "__main__":
    main()
    