from MaterialBiblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_paginas = numero_paginas
    
    def informacion(self):
        return super().informacion() + f", Número de Páginas: {self.numero_paginas}"