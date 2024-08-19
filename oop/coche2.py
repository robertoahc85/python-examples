# Definición de la clase
class Coche:
    # Método de inicialización (__init__)
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    # Método que imprime los detalles del coche
    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

# Inicialización de un objeto (instancia) de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2020)

# Llamada al método mostrar_detalles
mi_coche.mostrar_detalles()
