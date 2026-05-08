"""
Una compañía editorial produce tanto libros impresos como audio-libros en discos compactos.
Diseñe una clase denominada Publicación que almacene el título (cadena) y el precio (numérico real) de una publicación.
A partir de esta clase, derive dos clases: Libro a la cual le agregue el número de páginas (entero) y CD, a la cual
le agregue el tiempo de reproducción en minutos (numérico real). Cada una de las clases debe tener propiedades para acceder
a sus respectivos datos. Elabore un diagrama de clases UML indicando las relaciones de herencia y codifique un sistema
mediante el cual se generen instancias de las clases Libro y CD, donde el usuario capture sus datos y se inserten en libros
respectivos objetos. Diseñe la forma que se muestra a continuación.
"""


class Publicacion:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    def __str__(self):
        return f"Título: {self.__titulo}\nPrecio: ${self.__precio:.2f}"


class Libro(Publicacion):
    def __init__(self, titulo, precio, numero_de_paginas):
        super().__init__(titulo, precio)
        self.__numero_de_paginas = numero_de_paginas

    @property
    def numero_de_paginas(self):
        return self.__numero_de_paginas

    @numero_de_paginas.setter
    def numero_de_paginas(self, valor):
        self.__numero_de_paginas = valor

    def __str__(self):
        return f"{super().__str__()}\nPáginas: {self.__numero_de_paginas}"


class CD(Publicacion):
    def __init__(self, titulo, precio, tiempo_de_reproduccion):
        super().__init__(titulo, precio)
        self.__tiempo_de_reproduccion = tiempo_de_reproduccion

    @property
    def tiempo_de_reproduccion(self):
        return self.__tiempo_de_reproduccion

    @tiempo_de_reproduccion.setter
    def tiempo_de_reproduccion(self, valor):
        self.__tiempo_de_reproduccion = valor

    def __str__(self):
        return f"{super().__str__()}\nTiempo: {self.__tiempo_de_reproduccion} min"


mi_libro = Libro("Cien años de soledad", 25.50, 496)

mi_cd = CD("The Dark Side of the Moon", 15.99, 42.5)

print(mi_libro, "\n")

print(mi_cd, "\n")
