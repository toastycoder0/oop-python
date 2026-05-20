import subprocess

subprocess.run("clear")


def guardar_datos():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")

    with open("personas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Nombre {nombre}\n")
        archivo.write(f"Edad {edad}\n")
        archivo.write(f"Correo {correo}\n")
        archivo.write("---------------------------\n")

    print("Datos guardados correctamente.\n")


def mostrar_datos():
    try:
        with open("personas.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            print("\n--- DATOS ALMACENADOS ---")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe.\n")


while True:
    print("""
--- MENÚ ---
1) Guardar datos
2) Mostrar archivos
3) Salir
    """)

    option = input("Seleccione una opción: ")

    if option == "1":
        guardar_datos()
    elif option == "2":
        mostrar_datos()
    elif option == "3":
        print("Saliendo....")
        break
    else:
        print(f"La opción: '{option}' no es valida")
