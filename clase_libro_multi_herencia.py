class Producto:
    def __init__(self, costo, unidades):
        self.__costo = costo
        self.__unidades = unidades

    @property
    def costo(self):
        return self.__costo

    def __str__(self):
        return f"Costo: {self.__costo}\nUnidades: {self.__unidades}"

    def vender_unidad(self, cantidad):
        if cantidad <= self.__unidades:
            self.__unidades -= cantidad

    def agregar_unidad(self, cantidad):
        self.__unidades += cantidad


class ContenidoEditorial:
    def __init__(self, titulo, paginas):
        self.__titulo = titulo
        self.__paginas = paginas

    def __str__(self):
        return f"Título: {self.__titulo}\nUnidades: {self.__paginas}"

    def minutos_estimados_lectura(self):
        return self.__paginas * 2


class Libro(Producto, ContenidoEditorial):
    def __init__(self, titulo, paginas, costo, unidades, genero):
        Producto.__init__(self, costo, unidades)
        ContenidoEditorial.__init__(self, titulo, paginas)
        self.genero = genero

    def __str__(self):
        info_producto = Producto.__str__(self)
        info_contenido = ContenidoEditorial.__str__(self)

        return f"{info_contenido}\n{info_producto}\nGénero: {self.genero}"

    def generar_ticket_de_venta(self, cantidad):
        total = self.costo * cantidad
        tiempo_lectura = self.minutos_estimados_lectura() * cantidad

        self.vender_unidad(cantidad)

        return f"--- TICKET DE VENTA ---\n{ContenidoEditorial.__str__(self)}\nCantidad vendida: {cantidad}\nTotal a pagar: ${total}\nTiempo total de lectura estimada: {tiempo_lectura} minutos"


mi_libro = Libro("Psicología del Éxito", 350, 299, 10, "Autoayuda")
ticket = mi_libro.generar_ticket_de_venta(2)

print(mi_libro, "\n")
print(ticket)

