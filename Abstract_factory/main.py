from calculosmmm_factory import Calculosmmm
from mostrargraficas_factory import Mostrargraficas

#-----------------------------------------
#Client
#-----------------------------------------


def main():
    factory=Calculosmmm()

    calculos=factory.crear_calculos()

    for i in calculos:
        print(i.calcular())

    factory=Mostrargraficas()

    mostrar=factory.crear_graficas()

    for i in mostrar:
        i.grafica()


if __name__ == "__main__":
    main()
   