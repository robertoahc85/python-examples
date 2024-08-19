class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def describir(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"
    
    def arrancar(self):
        return f"El {self.marca} {self.modelo} está arrancando."

# Creación de un Objeto (Instancia de la Clase)
mi_coche = Coche("Toyota", "Corolla", 2020)

# Accediendo a los Métodos del Objeto
print(mi_coche.describir())  # Output: Coche: Toyota Corolla, Año: 2020
print(mi_coche.arrancar())   # Output: El Toyota Corolla está arrancando.
