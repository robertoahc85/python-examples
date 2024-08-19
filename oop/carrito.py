# Excepción personalizada
class StockInsuficienteError(Exception):
    pass

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_en_stock = cantidad_en_stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = valor

    @property
    def cantidad_en_stock(self):
        return self.__cantidad_en_stock

    @cantidad_en_stock.setter
    def cantidad_en_stock(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad en stock no puede ser negativa.")
        self.__cantidad_en_stock = cantidad

    def reducir_stock(self, cantidad):
        if cantidad > self.__cantidad_en_stock:
            raise StockInsuficienteError("Stock insuficiente para la cantidad solicitada.")
        self.__cantidad_en_stock -= cantidad

# Clase Carrito
class Carrito:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.__productos:
            self.__productos[producto.nombre]["cantidad"] += cantidad
        else:
            self.__productos[producto.nombre] = {
                "producto": producto,
                "cantidad": cantidad
            }

        try:
            producto.reducir_stock(cantidad)
        except StockInsuficienteError as e:
            print(f"Error al agregar {producto.nombre} al carrito: {e}")
            self.__productos[producto.nombre]["cantidad"] -= cantidad

    def eliminar_producto(self, nombre_producto):
        if nombre_producto in self.__productos:
            del self.__productos[nombre_producto]

    def calcular_total(self):
        total = 0
        for item in self.__productos.values():
            total += item["producto"].precio * item["cantidad"]
        return total

    def mostrar_carrito(self):
        if not self.__productos:
            print("El carrito está vacío.")
            return

        print("Carrito de Compras:")
        for item in self.__productos.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            print(f"{producto.nombre} - Cantidad: {cantidad}, Precio: ${producto.precio:.2f}")
        print(f"Total: ${self.calcular_total():.2f}")

# Prueba del sistema
try:
    p1 = Producto("Laptop", 1000, 5)
    p2 = Producto("Smartphone", 500, 10)
    p3 = Producto("Auriculares", 150, 2)

    carrito = Carrito()
    carrito.agregar_producto(p1, 2)
    carrito.agregar_producto(p2, 1)
    carrito.agregar_producto(p3, 3)  # Esto debería lanzar una excepción
    carrito.mostrar_carrito()

    carrito.eliminar_producto("Smartphone")
    carrito.mostrar_carrito()

except ValueError as e:
    print(f"Error: {e}")

