class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depósito realizado: ${cantidad}. Nuevo saldo: ${self.saldo}"
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        else:
            self.saldo -= cantidad
            return f"Retiro realizado: ${cantidad}. Nuevo saldo: ${self.saldo}"
    
    def consultar_saldo(self):
        return f"El saldo actual de {self.titular} es: ${self.saldo}"

# Creación de un Objeto (Instancia de la Clase)
cuenta = CuentaBancaria("Juan Pérez", 1000)

# Usando los Métodos del Objeto
print(cuenta.consultar_saldo())   # Output: El saldo actual de Juan Pérez es: $1000
print(cuenta.depositar(500))      # Output: Depósito realizado: $500. Nuevo saldo: $1500
print(cuenta.retirar(300))        # Output: Retiro realizado: $300. Nuevo saldo: $1200
print(cuenta.retirar(1500))       # Output: Fondos insuficientes.
