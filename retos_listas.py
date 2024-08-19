# NSTRUCCIONES

# Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.

# DESCRIPCIÓN

# Dada la siguiente lista de nombres:

# Marie Curie
# Cristiano Ronaldo
# Nikola Tesla
# Roger Federer
# Galileo Galilei
# Serena Williams
# Ada Lovelace
# Rafael Nadal
# Michael Jordan
# Y sabiendo que Marie Curie, Nikola Tesla, Galileo Galilei y Ada Lovelace son científicos. 
# También sabemos que Cristiano Ronaldo, Roger Federer, Serena Williams, Rafael Nadal y Michael Jordan son deportistas. 
# Debemos separar los nombres en tres grupos: científicos, deportistas y otros; y escribir una función llamada honrar_cientificos(), 
# que modifique la lista de científicos añadiendo la frase "El honorable" antes del nombre de cada científico.

# Crear una función llamada mostrar_nombres(), que imprima el nombre de cada persona de la lista.

# Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; 
# luego imprimir los nombres de los científicos honorables, los nombres de los deportistas y los restantes.

# Lista de nombres inicial

nombres = [
    "Marie Curie",
    "Cristiano Ronaldo",
    "Nikola Tesla",
    "Roger Federer",
    "Galileo Galilei",
    "Serena Williams",
    "Ada Lovelace",
    "Rafael Nadal",
    "Michael Jordan"
]

# Función para honrar a los científicos
def honrar_cientificos(cientificos):
    for i in range(len(cientificos)):
        cientificos[i] = "El honorable " + cientificos[i]

# Función para imprimir nombres
def mostrar_nombres(nombres):
    for nombre in nombres:
        print(nombre)





# Separación de nombres en grupos
cientificos = ["Marie Curie", "Nikola Tesla", "Galileo Galilei", "Ada Lovelace"]
deportistas = ["Cristiano Ronaldo", "Roger Federer", "Serena Williams", "Rafael Nadal", "Michael Jordan"]
# otros = [nombre for nombre in nombres if nombre not in cientificos and nombre not in deportistas]
otros = []
for nombre in nombres:
    if nombre not in cientificos and nombre not in deportistas:
        otros.append(nombre)


# Imprimir la lista completa de nombres antes de ser modificados
print("Lista completa de nombres antes de ser modificados:")
mostrar_nombres(nombres)

# Modificar la lista de científicos para honrarlos
honrar_cientificos(cientificos)

# Imprimir los nombres de los científicos honorables
print("\nCientíficos honorables:")
mostrar_nombres(cientificos)

# Imprimir los nombres de los deportistas
print("\nDeportistas:")
mostrar_nombres(deportistas)

# Imprimir los nombres restantes
print("\nOtros:")
mostrar_nombres(otros)
