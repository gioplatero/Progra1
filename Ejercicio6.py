# Crear un vector de 5 elementos de cadenas de caracteres
vector = []

for i in range(5):
    cadena = input("Ingrese una cadena de caracteres: ")
    vector.append(cadena)

#Copiar los elementos del vector en orden inverso
vector_inverso = vector[::-1]
print("Vector original:", vector)
print("Vector en orden inverso:", vector_inverso)