from calculos_factory import Calculos_estadistico
import pandas as pd

#Client
def main():
    df = pd.read_csv('emergencias.csv')
    factory = Calculos_estadistico()
    todos_los_calculos = factory.crear_calculos()
    print(f'media'{media.})


if __name__ == "__main__":
    main()

