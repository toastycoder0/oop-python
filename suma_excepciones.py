import os

os.system("clear")

numero_uno = None
numero_dos = None

while True:
    try:
        if numero_uno is None:
            numero_uno = int(input("Ingresa el primer número: "))

        if numero_dos is None:
            numero_dos = int(input("Ingresa el segundo número: "))

        division = numero_uno / numero_dos
        print(f"✅ Resultado: {division}")
        break

    except ValueError:
        if numero_uno is None:
            print("❌ Error en el PRIMER número. Intenta de nuevo.")
        else:
            print("❌ Error en el SEGUNDO número. Intenta de nuevo.")

    except ZeroDivisionError:
        print("❌ Error: El segundo número no puede ser 0.")
        numero_dos = None
