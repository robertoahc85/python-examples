class Libro:
    def __init__(self, titulo, autor, paginas):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._disponible = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._paginas = valor
        else:
            print("Error: El número de páginas debe ser un entero positivo.")

    @property
    def disponible(self):
        return self._disponible

    @property
    def info(self):
        estado = "disponible" if self._disponible else "prestado"
        return f"{self._titulo} por {self._autor}, {self._paginas} páginas. Estado: {estado}"

    def prestar(self):
        if self._disponible:
            self._disponible = False
            print(f"El libro '{self._titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self._titulo}' no está disponible en este momento.")

    def devolver(self):
        if not self._disponible:
            self._disponible = True
            print(f"El libro '{self._titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self._titulo}' ya estaba en la biblioteca.")

# Uso de la clase
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 432)

# Uso de propiedades de solo lectura
print(libro1.titulo)    # Cien años de soledad
print(libro1.autor)     # Gabriel García Márquez

# Uso de propiedad con setter
print(libro1.paginas)   # 432
libro1.paginas = 433
print(libro1.paginas)   # 433

libro1.paginas = -100   # Esto imprimirá un mensaje de error sin lanzar una excepción

# Uso de propiedad calculada
print(libro1.info)      # Cien años de soledad por Gabriel García Márquez, 433 páginas. Estado: disponible

# Uso de métodos que modifican una propiedad
libro1.prestar()        # El libro 'Cien años de soledad' ha sido prestado.
print(libro1.disponible)  # False

libro1.prestar()        # El libro 'Cien años de soledad' no está disponible en este momento.

libro1.devolver()       # El libro 'Cien años de soledad' ha sido devuelto.
print(libro1.disponible)  # True

libro1.devolver()       # El libro 'Cien años de soledad' ya estaba en la biblioteca.