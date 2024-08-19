#Clase
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def ladrar(self):  # Método de instancia
        print("¡Woof!")
#objeto
mi_perro = Perro("Fido", 3)
print(mi_perro.nombre)  # Imprime "Fido"
mi_perro.ladrar()       # Imprime "¡Woof!"

#metodos 
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice ¡Woof!")



#class Perro:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo privado (convención)
        self._edad = edad

    def _ladrar(self):  # Método privado (convención)
        print(f"{self._nombre} dice ¡Woof!")
        
#Encapsulamiento
class Perro:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo privado (convención)
        self._edad = edad

    def _ladrar(self):  # Método privado (convención)
        print(f"{self._nombre} dice ¡Woof!")
       
from abc import ABC, abstractmethod
# Abstracción
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

# El polimorfismo 
class Perro(Animal):
    def hacer_sonido(self):
        print("¡Woof!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")
        
class Perro:
    def hacer_sonido(self):
        print("¡Woof!")

class Gato:
    def hacer_sonido(self):
        print("¡Miau!")

def hacer_sonido_animal(animal):
    animal.hacer_sonido()

mi_perro = Perro()
mi_gato = Gato()

hacer_sonido_animal(mi_perro)  # Imprime "¡Woof!"
hacer_sonido_animal(mi_gato)   # Imprime "¡Miau!"
        
        





# En Python, la abstracción se puede lograr utilizando clases abstractas y métodos abstractos
# que definen una interfaz para las clases derivadas:


from abc import ABC, abstractmethod

class Forma(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):  # Clase concreta que implementa la abstracción
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)
    
#  La encapsulación asegura que los detalles internos de un objeto están ocultos al mundo exterior,
#  y que el acceso a ellos se realiza a través de una interfaz pública:


class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, monto):
        self.__saldo += monto

    def obtener_saldo(self):
        return self.__saldo   
    