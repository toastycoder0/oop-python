# Hacer un programa que muestre un menu de opciones con las siguientes opciones:
# Opcion 1 agregar elemento
# Opcion 2 eliminar elemento
# Opcion 3 mostrar elementos
# Opcion 4 Salir
import os

os.system("clear")

lista = []


while True:
    print("""
Opciones: 
1) Agregar elemento
2) Eliminar elemento
3) Mostrar elementos
4) Salir
    """)
    opcion = int(input("Secciona una opción: "))

    if opcion == 1:
        nuevo_elemento = int(input("Ingresa el nuevo elemento: "))
        lista.append(nuevo_elemento)
    elif opcion == 2:
        elemento_a_eliminar = int(input("Ingresa el elemento a eliminar: "))
        if elemento_a_eliminar in lista:
            lista.remove(elemento_a_eliminar)
        else:
            print("Elemento no encontrado")
    elif opcion == 3:
        print("Lista:")
        for elemento in lista:
            print(elemento)
    elif opcion == 4:
        break
    else:
        print("Opción no disponible")
