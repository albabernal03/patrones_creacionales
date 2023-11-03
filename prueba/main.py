from elegircal import MMM
from caculosfecha_provider import Calculosfechaprovider

# Client

def main():
    elegircal = MMM.MEDIA

    factory = Calculosfechaprovider.create_calculos(elegircal)
    calcular_media = factory.calcular()
    
    print(f'media: {calcular_media}')

if __name__ == "__main__":
    main()