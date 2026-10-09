# Etapa 4: Ordenamiento
lista_numeros = [34, 7, 23, 32, 5, 62, 18, 11]
print("Lista original:", lista_numeros)

burbuja = lista_numeros.copy()
n = len(burbuja)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if burbuja[j] > burbuja[j + 1]:
            temp = burbuja[j]
            burbuja[j] = burbuja[j + 1]
            burbuja[j + 1] = temp

print("Despues de burbuja:")
print(burbuja)

seleccion = lista_numeros.copy()
n = len(seleccion)

for i in range(n - 1):
    menor = i
    for j in range(i + 1, n):
        if seleccion[j] < seleccion[menor]:
            menor = j
    temp = seleccion[i]
    seleccion[i] = seleccion[menor]
    seleccion[menor] = temp

print("Despues de seleccion:")
print(seleccion)

print("Original :", lista_numeros)
print("Burbuja  :", burbuja)
print("Seleccion:", seleccion)
print("Iguales:", burbuja == seleccion)
