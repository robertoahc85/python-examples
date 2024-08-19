from MaterialBiblioteca import MaterialBiblioteca

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_edicion = numero_edicion
    
    def informacion(self):
        return super().informacion() + f", Número de Edición: {self.numero_edicion}"