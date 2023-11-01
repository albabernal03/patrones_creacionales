from calculos_factory import Calculos_estadistico

#Client
def main():
    factory = calculos_factory()
    calculosestadisticos = factory.crear_calculos()

    # Simular la entrada del usuario seleccionando la opción 1
    opcion = 1

    # Verificar si la opción ingresada por el usuario es válida
    if opcion == 1:
        columna_seleccionada = 'FECHA_NUM'
    elif opcion == 2:
        columna_seleccionada = 'ID-EVENTO'
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
        return

    # Crear la gráfica de barras utilizando la columna seleccionada
    df[columna_seleccionada].value_counts().plot(kind='bar')

    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    main()

