class Cuenta:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")
    
    def __calcular_interes(self):  # Método privado
        return self.__saldo * 0.05

class CuentaAhorro(Cuenta):
    def aplicar_interes(self):
        interes = self._Cuenta__calcular_interes()  # Acceso a método privado de la clase padre
        self.depositar(interes)