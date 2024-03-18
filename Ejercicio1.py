def crear_array_multiplos(tamaño, numero):
    return [numero * i for i in range(1, tamaño + 1)]

tamaño = int(input("Ingrese el tamaño del array: "))
numero = int(input("Ingrese el número del que desea obtener los múltiplos: "))

array_multiplos = crear_array_multiplos(tamaño, numero)
print("Array con múltiplos de", numero, ":", array_multiplos)