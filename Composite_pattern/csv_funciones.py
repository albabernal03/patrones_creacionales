from combo import Combo
from combo_pareja import ComboPareja
from pizza import Pizza
from bebida import Bebida
from entrante import Entrante
from postre import Postre

def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    column_names = ["Usuario", "Tipo", "Nombre", "Precio"]

    with open(nombre_archivo, 'a') as archivo:
       
        if archivo.tell() == 0:
            archivo.write(','.join(column_names) + '\n')

        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            for subelemento in elemento.elementos:
                guardar_elemento_csv(subelemento, nombre_archivo, usuario)
        elif isinstance(elemento, ComboPareja):
            archivo.write(f'{usuario},ComboPareja,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            if elemento.combo1:
                guardar_elemento_csv(elemento.combo1, nombre_archivo, usuario)
            if elemento.combo2:
                guardar_elemento_csv(elemento.combo2, nombre_archivo, usuario)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            archivo.write(f'{usuario},{type(elemento).__name__},{elemento.nombre},{elemento.precio}\n')



def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    with open(nombre_archivo, 'a') as archivo:
        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            for subelemento in elemento.elementos:
                guardar_elemento_csv(subelemento, nombre_archivo, usuario)
        elif isinstance(elemento, ComboPareja):
            archivo.write(f'{usuario},ComboPareja,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            if elemento.combo1:
                guardar_elemento_csv(elemento.combo1, nombre_archivo, usuario)
            if elemento.combo2:
                guardar_elemento_csv(elemento.combo2, nombre_archivo, usuario)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            archivo.write(f'{usuario},{type(elemento).__name__},{elemento.nombre},{elemento.precio}\n')

def leer_elementos_csv(nombre_archivo, usuario):
    elementos = []
    combos = {}

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            usuario_archivo, tipo_elemento, nombre_elemento, precio_elemento = linea.strip().split(',')
            if usuario_archivo == usuario:
                if tipo_elemento == 'Combo':
                    combo = Combo(nombre_elemento)
                    combos[nombre_elemento] = combo
                    elementos.append(combo)
                elif tipo_elemento == 'ComboPareja':
                    combo_pareja = ComboPareja(nombre_elemento)
                    combo_pareja.combo1 = combos.get(nombre_elemento + "_1")
                    combo_pareja.combo2 = combos.get(nombre_elemento + "_2")
                    elementos.append(combo_pareja)
                elif tipo_elemento in ['Pizza', 'Bebida', 'Entrante', 'Postre']:
                    clase_elemento = globals()[tipo_elemento]
                    elemento = clase_elemento(nombre_elemento, float(precio_elemento))
                    elementos.append(elemento)

    return elementos




def preguntar_guardar_historial():
    while True:
        respuesta = input("¿Deseas guardar el historial de pedidos? (s/n): ").lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

def reconstruir_menu_desde_historial(nombre_archivo, usuario):
    elementos = leer_elementos_csv(nombre_archivo, usuario)
    menu_reconstruido = []

    for elemento in elementos:
        if isinstance(elemento, Combo):
            combo_reconstruido = Combo(elemento.nombre)
            for subelemento in elemento.elementos:
                subelemento_reconstruido = reconstruir_elemento_desde_historial(subelemento, elementos)
                combo_reconstruido.agregar_elemento(subelemento_reconstruido)
            menu_reconstruido.append(combo_reconstruido)
        elif isinstance(elemento, ComboPareja):
            combo_pareja_reconstruido = ComboPareja(elemento.nombre)
            combo_pareja_reconstruido.combo1 = reconstruir_elemento_desde_historial(elemento.combo1, elementos)
            combo_pareja_reconstruido.combo2 = reconstruir_elemento_desde_historial(elemento.combo2, elementos)
            menu_reconstruido.append(combo_pareja_reconstruido)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            elemento_reconstruido = reconstruir_elemento_desde_historial(elemento, elementos)
            menu_reconstruido.append(elemento_reconstruido)

    return menu_reconstruido


def reconstruir_elemento_desde_historial(elemento, elementos):
    if isinstance(elemento, Combo):
        combo_reconstruido = Combo(elemento.nombre)
        for subelemento in elemento.elementos:
            subelemento_reconstruido = reconstruir_elemento_desde_historial(subelemento, elementos)
            combo_reconstruido.agregar_elemento(subelemento_reconstruido)
        return combo_reconstruido
    elif isinstance(elemento, ComboPareja):
        combo_pareja_reconstruido = ComboPareja(elemento.nombre)
        combo_pareja_reconstruido.combo1 = reconstruir_elemento_desde_historial(elemento.combo1, elementos)
        combo_pareja_reconstruido.combo2 = reconstruir_elemento_desde_historial(elemento.combo2, elementos)
        return combo_pareja_reconstruido
    elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
        return elemento
