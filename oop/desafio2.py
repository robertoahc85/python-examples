class MaterialBiblioteca:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self._año_publicacion = año_publicacion

    @property
    def año_publicacion(self):
        return self._año_publicacion

    @año_publicacion.setter
    def año_publicacion(self, valor):
        if valor > 2024:
            raise ValueError("El año de publicación no puede estar en el futuro.")
        self._año_publicacion = valor

    def informacion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.año_publicacion}."


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_paginas = numero_paginas

    def informacion(self):
        info_base = super().informacion()
        return f"{info_base} Tiene {self.numero_paginas} páginas."


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_edicion = numero_edicion

    def informacion(self):
        info_base = super().informacion()
        return f"{info_base} Es la edición número {self.numero_edicion}."


class Periodico(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, fecha):
        super().__init__(titulo, autor, año_publicacion)
        self.fecha = fecha

    def informacion(self):
        info_base = super().informacion()
        return f"{info_base} Fecha de publicación: {self.fecha}."


# Ejemplo de uso
libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 471)
revista = Revista("National Geographic", "Varios", 2023, 88)
periodico = Periodico("El País", "Varios", 2024, "12/08/2024")

print(libro.informacion())
print(revista.informacion())
print(periodico.informacion())
