
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
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}"





