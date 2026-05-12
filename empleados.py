class Empleado:
    def __init__(
        self, nombre, apellidos, dni, direccion, telefono, salario, supervisor
    ):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
        self.__salario = salario
        self.__supervisor = supervisor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self.__apellidos = valor

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
        self.__dni = valor

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = valor

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        self.__salario = valor

    @property
    def supervisor(self):
        return self.__supervisor
    
    @supervisor.setter
    def supervisor(self, valor):
        self.__supervisor = valor

    def __str__(self):
        texto = f"Empleado: {self.__nombre} {self.__apellidos}\nDNI: {self.__dni}\nDirección: {self.__direccion}\nTeléfono: {self.__telefono}Salario: {self.__salario}"
        if self.__supervisor:
            texto += f"Supervisor: {self.__supervisor}"
        return texto

    def cambiar_supervisor(self, nuevo_supervisor):
        self.__supervisor = nuevo_supervisor

    def incrementar_salario(self, porcentaje):
        self.__salario *= 1 + porcentaje / 100


class Secretario(Empleado):
    def __init__(
        self,
        nombre,
        apellidos,
        dni,
        direccion,
        telefono,
        salario,
        despacho,
        fax,
        supervisor=None,
    ):
        super().__init__(
            nombre, apellidos, dni, direccion, telefono, salario, supervisor
        )
        self.__despacho = despacho
        self.__fax = fax

    @property
    def despacho(self):
        return self.__despacho

    @despacho.setter
    def despacho(self, valor):
        self.__despacho = valor

    @property
    def fax(self):
        return self.__fax

    @fax.setter
    def fax(self, valor):
        self.__fax = valor

    def incrementar_salario(self):
        super().incrementar_salario(5)

    def __str__(self):
        return f"{super().__str__()}\nDespacho: {self.__despacho}\nFax: {self.__fax}"


class Vendedor(Empleado):
    def __init__(
        self,
        nombre,
        apellidos,
        dni,
        direccion,
        telefono,
        salario,
        coche,
        movil,
        area_venta,
        comision,
        supervisor,
    ):
        super().__init__(
            nombre, apellidos, dni, direccion, telefono, salario, supervisor
        )
        self.__coche = coche
        self.__movil = movil
        self.__area_venta = area_venta
        self.__comision = comision
        self.__clientes = []

    @property
    def coche(self):
        return self.__coche
    
    @coche.setter
    def coche(self, valor):
        self.__coche = valor

    @property
    def movil(self):
        return self.__movil
    
    @movil.setter
    def movil(self, valor):
        self.__movil = valor

    @property
    def area_venta(self):
        return self.__area_venta

    @area_venta.setter
    def area_venta(self, valor):
        self.__area_venta = valor

    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self, valor):
        self.__comision = valor

    @property
    def clientes(self):
        return self.__clientes
    
    @clientes.setter
    def clientes(self, valor):
        self.__clientes = valor

    
    def incrementar_salario(self):
        super().incrementar_salario(10)

    def __str__(self):
        return f"{super().__str__()}\nCoche: {self.__coche}\nMóvil: {self.__movil}\nÁrea de venta: {self.__area_venta}\nComisión: {self.__comision}%\nClientes: {self.__clientes}"

    def dar_alta_cliente(self, cliente):
        self.__clientes.append(cliente)

    def dar_baja_cliente(self, cliente):
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)

    def cambiar_coche(self, nuevo_coche):
        self.__coche = nuevo_coche


class JefeDeZona(Empleado):
    def __init__(
        self,
        nombre,
        apellidos,
        dni,
        direccion,
        telefono,
        salario,
        despacho,
        coche,
        secretario,
        vendedores,
    ):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario, None)
        self.__despacho = despacho
        self.__coche = coche
        self.__secretario = secretario
        self.__vendedores = vendedores

    @property
    def despacho(self):
        return self.__despacho
    
    @despacho.setter
    def despacho(self, valor):
        self.__despacho = valor

    @property
    def coche(self):
        return self.__coche
    
    @coche.setter
    def coche(self, valor):
        self.__coche = valor

    @property
    def secretario(self):
        return self.__secretario
    
    @secretario.setter
    def secretario(self, valor):
        self.__secretario = valor

    @property
    def vendedores(self):
        return self.__vendedores
    
    @vendedores.setter
    def vendedores(self, valor):
        self.__vendedores = valor

    def incrementar_salario(self):
        super().incrementar_salario(20)

    def __str__(self):
        texto = (
            f"{super().__str__()}\nDespacho: {self.__despacho}\nCoche: {self.__coche}"
        )
        if self.__secretario:
            texto += f"\nSecretario: {self.__secretario}"

        if len(self.__vendedores) > 0:
            texto += "\n\nVendedores a cargo:\n"
            for vendedor in self.__vendedores:
                texto += f"- {vendedor}\n\n"
        return texto

    def cambiar_secretario(self, nuevo_secretario):
        self.__secretario = nuevo_secretario

    def cambiar_coche(self, nuevo_coche):
        self.__coche = nuevo_coche

    def dar_alta_vendedor(self, vendedor):
        self.__vendedores.append(vendedor)

    def dar_baja_vendedor(self, vendedor):
        if vendedor in self.__vendedores:
            self.__vendedores.remove(vendedor)


secretario = Secretario(
    "Ana",
    "Gomez",
    "12345678A",
    "Calle Falsa 123",
    "600123456",
    2000,
    "Despacho 1",
    "912345678",
)

vendedor = Vendedor(
    "Luis",
    "Perez",
    "87654321B",
    "Calle Real 45",
    "600654321",
    1500,
    "Ford modelo Focus 1234XYZ",
    "600987654",
    "Zona Norte",
    5,
    None,
)

jefe_de_zona = JefeDeZona(
    "Carlos",
    "Lopez",
    "11223344C",
    "Av. Central 10",
    "601234567",
    3000,
    "Despacho Jefe",
    {"matricula": "9999AAA", "marca": "BMW", "modelo": "X5"},
    secretario=secretario,
    vendedores=[vendedor],
)

secretario.incrementar_salario()
vendedor.incrementar_salario()
jefe_de_zona.incrementar_salario()

vendedor.dar_alta_cliente("Cliente 1")
vendedor.dar_alta_cliente("Cliente 2")

jefe_de_zona.dar_alta_vendedor(
    Vendedor(
        "Marta",
        "Diaz",
        "55555555D",
        "Calle Luna 5",
        "602345678",
        1600,
        {"matricula": "5678BCD", "marca": "Audi", "modelo": "A3"},
        "602987654",
        "Zona Sur",
        6,
        None,
    )
)

print(f"\n--- Empleados ---\n\n{secretario}\n\n{vendedor}\n\n{jefe_de_zona}")
