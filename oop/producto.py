# Definición de la clase
class Producto:
    # Método de inicialización (__init__)
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Método para mostrar detalles del producto
    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}")

    # Método para agregar más stock del producto
    def agregar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Se han agregado {cantidad} unidades de {self.nombre}. Cantidad actual: {self.cantidad}")

    # Método para vender unidades del producto
    def vender(self, cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficiente stock de {self.nombre}. Solo hay {self.cantidad} unidades disponibles.")
        else:
            self.cantidad -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Cantidad actual: {self.cantidad}")

# Inicialización de un objeto (instancia) de la clase Producto
producto1 = Producto("Laptop", 1500, 10)

# Llamada a los métodos mostrar_detalles, agregar_stock y vender
producto1.mostrar_detalles()
producto1.agregar_stock(5)
producto1.vender(3)
producto1.mostrar_detalles()
