#Etapa 2: Exploración de listas/arreglos bidimensionales
def Arreglo_bidimensional():
        print("Arreglos bidimensionales")
filas = 3
columnas = 3
matriz = []
suma = 0
for i in range(filas):
        fila = []
        for j in range(columnas):
                fila.append(int(input(f"Ingrese el valor para la posicion [{i}][{j}]: ")))
        matriz.append(fila)
for fila in matriz:
        print(fila)
for i in range(filas):
        for j in range(columnas):
                suma += matriz[i][j]
promedio = suma/(filas*columnas)
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")



