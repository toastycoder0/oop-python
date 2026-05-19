"""
Crear un programa que almacene 5 numeros enteros inicialmente leidos desde el teclado almacenarlos en una lista
poner un menu que permita:
1) Agregar elementos
2) Eliminar elementos
3) Buscar un elementos de la lista de acuerdo a su posicion
4) Salir
Agregar la excepcion IndexError y la excepcion ValueError
"""

import os


os.system("clear")

numeros = []


def agregar():
    try:
        numero_nuevo = int(input("Ingresa el número a agregar: "))
        numeros.append(numero_nuevo)
        print(f"Número {numero_nuevo} agregado en la posición {len(numeros) - 1}")
    except Exception:
        raise TypeError("El valor tiene que se un número entero")


def eliminar():
    try:
        numero_nuevo = int(input("Ingresa el número a eliminar: "))
    except Exception:
        raise TypeError("El valor tiene que se un número entero")
    if numero_nuevo in numeros:
        numeros.remove(numero_nuevo)
        print(f"Número {numero_nuevo} eliminado de la lista")
        return
    raise IndexError("El número no esta en la lista")


def buscar():
    try:
        indice_a_buscar = int(input("Ingresa el número a agregar: "))
    except Exception:
        raise TypeError("El valor tiene que se un número entero")
    for indice in range(0, len(numeros)):
        if indice == indice_a_buscar:
            print(f"El número en el indice {indice_a_buscar} es {numeros[indice]}")
            return
    raise IndexError(f"No existe un número en el indice {indice_a_buscar}")


def programa():
    try:
        for numero in range(1, 6):
            numero_ingresado = int(input(f"Ingresa el número {numero}: "))
            numeros.append(numero_ingresado)
            print(f"Número {numero_ingresado} ingresado en la posición {numero - 1}")

        while True:
            print("""
Opciones:
1) Agregar un elemento
2) Eliminar un elemento
3) Buscar un elementos de la lista de acuerdo a su posicion
4) Salir
            """)

            opcion = input("Ingresa una opción: ")

            if opcion == "1":
                agregar()
            elif opcion == "2":
                eliminar()
            elif opcion == "3":
                buscar()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print(f"La opción '{opcion}' no existe")

    except (IndexError, ValueError) as error_manejado:
        print(error_manejado)
    except Exception:
        print("Error desconocido")


programa()
