import os


class Cuenta:
    def __init__(self, cuenta, saldo_inicial):
        self.__cuenta = cuenta
        self.__saldo = saldo_inicial

    @property
    def cuenta(self):
        return self.__cuenta

    @cuenta.setter
    def cuenta(self, valor):
        self.__cuenta = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def consultar(self):
        return self.saldo

    def depositar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except ValueError:
            raise TypeError("El depósito debe ser un número válido.")
        if cantidad <= 0:
            raise ValueError("El depósito debe ser mayor que cero.")
        self.saldo += cantidad

    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except ValueError:
            raise TypeError("El retiro debe ser un número válido.")
        if cantidad <= 0:
            raise ValueError("El retiro debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= cantidad


os.system("clear")

mi_cuenta = Cuenta("12345", 1000.0)

while True:
    print("""
1) Consultar saldo
2) Depositar
3) Retirar
4) Salir
    """)
    opcion = input("Ingresa una opción: ")

    try:
        if opcion == "1":
            print(f"Tu saldo actual es: ${mi_cuenta.consultar():.2f}")

        elif opcion == "2":
            cantidad = input("Ingresa la cantidad a depositar: ")
            mi_cuenta.depositar(cantidad)
            print(f"Depósito exitoso. Saldo actual: ${mi_cuenta.consultar():.2f}")

        elif opcion == "3":
            cantidad = input("Ingresa la cantidad a retirar: ")
            mi_cuenta.retirar(cantidad)
            print(f"Retiro exitoso. Saldo actual: ${mi_cuenta.consultar():.2f}")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

    except (ValueError, TypeError) as error_manejado:
        print(error_manejado)
    except Exception:
        print("Ocurrió un error inesperado")
