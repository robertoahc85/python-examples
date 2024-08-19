# Comprobación en Listas
frutas = ["manzana", "banana", "cereza"]
if "banana" in frutas:
    print("La banana está en la lista de frutas.")
    
#  Comprobación en Cadenas de Texto
mensaje = "Hola, mundo"
if "mundo" in mensaje:
    print("La palabra 'mundo' está en el mensaje.")   
    
  #tupla  
numeros = (1, 2, 3, 4, 5)
if 3 in numeros:
    print("El número 3 está en la tupla.")
    
 #cojuntos   
colores = {"rojo", "verde", "azul"}
if "verde" in colores:
    print("El color verde está en el conjunto.")
#Diccionario
if "edad" in estudiante:
    print("La clave 'edad' está en el diccionario.")
# Comprobación Negativa

nombres = ["Ana", "Luis", "Carlos"]
if "Juan" not in nombres:
    print("Juan no está en la lista.")   

# Uso en Bucles
for letra in "python":
    if letra in "aeiou":
        print(f"{letra} es una vocal.")  
   