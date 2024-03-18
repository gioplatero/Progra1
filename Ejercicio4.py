A= [20, 15, 12, 11, 8, 4, 1]
menor = A[0] 
for i in A: 
    if i < menor: menor = i

A_sin_menor = [nota for nota in A if nota != menor]

print("Nota más baja eliminada:", menor) 
print("Lista de notas sin la nota más baja:", A_sin_menor)
suma_sin_menor = sum(A_sin_menor) 
promedio = suma_sin_menor / (len(A_sin_menor) if len(A_sin_menor) > 0 else 1)

print("Promedio de notas descontando la nota eliminada:", promedio)