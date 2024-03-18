notas = []

for i in range(5): 
    nota = float(input("Ingrese la nota " + str(i+1) + " (0 a 10): ")) 
    if nota < 0 or nota > 10: 
        print("La nota debe ser un valor entre 0 y 10.") 
        i -= 1 
        continue 
    notas.append(nota)
nota_media = sum(notas) / len(notas)
nota_maxima = max(notas) 
nota_minima = min(notas)
print("Notas:", notas) 
print("Nota media:", nota_media) 
print("Nota más alta:", nota_maxima) 
print("Nota más baja:", nota_minima)