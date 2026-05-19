class EdadInvalidaError(ValueError):
    """Error lanzado cuando la edad ingresada no es válida."""


def validar_edad(edad):
    """
    Valida que la edad esté dentro de un rango razonable.
    """

    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")

    if edad > 120:
        raise EdadInvalidaError("La edad ingresada no es válida.")

    return edad


def main():
    try:
        edad = int(input("Ingresa tu edad: "))

        validar_edad(edad)

        print(f"Edad registrada correctamente: {edad}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

