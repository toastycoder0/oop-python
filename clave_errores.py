"""
Hacer un programa que solicite al usuario una contraseña y analice si la contraseña es valida considerando las siguientes condiciones:
1) Tener minimo 8 caracteres de longitud
2) Tener una letra mayuscula
3) Tener una letra minuscula
4) Tener un caracter especial
El programa debe lanzar una excepcion de contraseña invalida y decirte si es valida o no
"""

import os

os.system("clear")

clave_a_probar = ""


class ClaveInvalidaError(TypeError):
    """Error lanzado cuando la contraseña ingresada no es válida."""


def tiene_longitud_valida():
    return len(clave_a_probar) > 7


def tiene_caracter_especial():
    for letra in clave_a_probar:
        if ord(letra) in range(33, 48):
            return True

        if ord(letra) in range(58, 65):
            return True

        if ord(letra) in range(91, 97):
            return True

        if ord(letra) in range(123, 127):
            return True

    return False


def esta_en_rango(inicial, final):
    for letra in clave_a_probar:
        if ord(letra) in range(inicial, final):
            return True
    return False


def tiene_signo(signo):
    return signo in clave_a_probar


def validar_clave():
    global clave_a_probar

    while True:
        try:
            clave_a_probar = input("Introduce la contraseña a evaluar: ")

            if not tiene_longitud_valida():
                raise ClaveInvalidaError(
                    "La contraseña debe tener más de 8 caracteres\n"
                )

            if not esta_en_rango(97, 122):
                raise ClaveInvalidaError(
                    "La contraseña debe contener al menos una minuscula\n"
                )

            if not esta_en_rango(65, 91):
                raise ClaveInvalidaError(
                    "La contraseña debe contener al menos una mayuscula\n"
                )

            if not tiene_caracter_especial():
                raise ClaveInvalidaError(
                    "La contraseña debe contener al menos un caracter especial\n"
                )

            print("La contraseña cumple con los parametros de seguridad")
            break
        except TypeError as error_manejado:
            print(error_manejado)
            continue


validar_clave()
