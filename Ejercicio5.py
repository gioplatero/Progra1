import random
arreglo_numeros = [0] * 10
for i in range(10):
    arreglo_numeros[i] = random.randint(1,10)
for  num in arreglo_numeros:
    cuadrado =  num ** 2
    cubo = num ** 3 
    print("El numero {} tiene su cuadrado en {}, y el cubo es {}".format(num,cuadrado,cubo))
    