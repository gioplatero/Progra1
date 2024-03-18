A = int(input("Ingrese el tamaño de los arreglos: "))
B = []
C = []
for  i in range (0,A):
    B.append(input("ingrese nombre de las personas: "))
    print ("Nombres de las personas son : ", B)
for j  in range (0,A):
    C.append(len(B[j]))
    print ("La longitud de cada nombre es: ", C[j])
