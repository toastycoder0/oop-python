"""
1) Hacer un programa que implemente TypeError
2) Hacer un programa que implemente KeyError
3) Hacer un programa que implemente OverFlowError (de recomendación un factorial)
4) Hacer un programa que implemente KeyboardInterrupt
"""

import math
import os

os.system("clear")

alumnos = []
calificaciones = {}


def agregar_alumno():
    nombre = input("\nIngresa el nombre del alumno: ")

    if nombre in alumnos:
        print("Ya hay una alumno con ese nombre registrado")
        return

    calificaciones_del_alumno = []

    for materia in range(3):
        calificacion = int(input(f"Ingresa la calificación {materia + 1} del alumno: "))
        calificaciones_del_alumno.append(calificacion)

    alumnos.append(nombre)
    calificaciones[nombre] = calificaciones_del_alumno

    print(f"Alumno {nombre} agregado")


def mostrar_alumnos():
    if len(alumnos) > 0:
        for alumno in alumnos:
            print(f"\nAlumno: {alumno}")
            try:
                for calificacion_indice in range(len(calificaciones[alumno])):
                    print(
                        f"Calificación {calificacion_indice + 1}: {calificaciones[alumno][calificacion_indice]}"
                    )
            except TypeError:
                print(
                    "Error: Las calificaciones de este alumno no son una lista válida"
                )
    else:
        print("No hay alumnos registrados")


def eliminar_alumno():
    nombre = input("\nIngresa el nombre del alumno a eliminar: ")
    try:
        alumnos.remove(nombre)
        del calificaciones[nombre]
        print(f"Alumno {nombre} eliminado")
    except KeyError:
        print(f"Error: El alumno {nombre} no existe en el registro")


def mostrar_promedios():
    print("\n")
    if len(alumnos) > 0:
        for alumno in alumnos:
            try:
                promedio = sum(calificaciones[alumno]) / len(calificaciones[alumno])
                print(f"Alumno {alumno} con promedio de {promedio}")
            except KeyError:
                print(f"Error: No se encontraron calificaciones para {alumno}")
    else:
        print("No hay alumnos registrados")


def generar_codigo_factorial():
    try:
        numero = int(
            input("\nIngresa la matrícula numérica para generar código verificador: ")
        )
        codigo = float(math.factorial(numero))
        print(f"Código generado: {codigo}")
    except OverflowError:
        print("Error: La matrícula es muy alta para calcular el código")


def menu():
    while True:
        try:
            print("""
Opciones

1) Agregar alumno
2) Mostrar alumnos
3) Eliminar alumno
4) Mostrar promedios
5) Generar código (Factorial)
6) Salir
            """)

            opcion = int(input("Ingresa una opción: "))

            if opcion == 1:
                agregar_alumno()
            elif opcion == 2:
                mostrar_alumnos()
            elif opcion == 3:
                eliminar_alumno()
            elif opcion == 4:
                mostrar_promedios()
            elif opcion == 5:
                generar_codigo_factorial()
            elif opcion == 6:
                print("Saliendo....")
                break
            else:
                print(f"La opción ingresada {opcion} no esta disponible")

        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
            break


menu()
