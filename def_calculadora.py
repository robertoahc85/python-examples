def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():
    print("Bienvenido a la Calculadora Python")
    
    while True:
        print("\nSelecciona una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Ingresa tu opción (1-5): ")
        
        if opcion == '1':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = sumar(num1, num2)
            print(f"El resultado de {num1} + {num2} es: {resultado}")
        
        elif opcion == '2':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = restar(num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        
        elif opcion == '3':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = multiplicar(num1, num2)
            print(f"El resultado de {num1} * {num2} es: {resultado}")
        
        elif opcion == '4':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es: {resultado}")
        
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intenta de nuevo.")

calculadora()
