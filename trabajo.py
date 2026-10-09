#Etapa 1: Exploración de listas/arreglos unidimensionales
def Explorar_lista():
        print("Listado de datos")
datos =[]
for i in range(10):
        print(f"Ingrese un numero para la posicion: {i + 1}")
        datos.append(int(input()))
for i in range(len(datos)):
        print(f"Elemento en posicion {i + 1}: {datos[i]}")

modificar_valor = int(input("Ingrese valor a modificar en la tercera posicion: "))
datos[2] = modificar_valor
print("Lista modificada", datos)

buscar_numero = int(input("Ingrese un numero a buscar en la lista: "))
if buscar_numero in datos:
        print(f"El numero {buscar_numero} esta en la lista")
else:
        print(f"El numero {buscar_numero} no esta en la lista")

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

# Etapa 3: Operaciones sobre listas
lista = [10, 20, 30, 40, 50]
print("lista inicial: ", lista)

print("1. Insertar un elemento en la lista")            
print("2. Eliminar un elemento de la lista")
print("3. Buscar un elemento en la lista")
print("4. Mostrar la lista actualizada")
opciones = int(input("Ingrese una de las 4 opciones (1-4): ")) 

if opciones == 1:
        valor = int(input("Ingrese el valor a insertar: "))
        lista.append(valor)
        print("Lista antes de insertar: ", lista)
elif opciones == 2:
        posicion = int(input("Ingrese la posición del elemento a eliminar (1-5): "))
        lista.pop(posicion - 1)
        print("Lista después de eliminar: ", lista)
elif opciones == 3:
        valor = int(input("Ingrese el valor a buscar: "))
        for i in range(len(lista)):
                if lista[i] == valor:
                        posicion = i
                        break 
                else:
                        print(f"El valor {valor} no se encuentra en la lista.")
elif opciones == 4:
        print("Lista actualizada: ", lista)
else:
        print("Opción inválida.")    


#Etapa 4: Aplicación de algoritmos de ordenamiento
lista_ordenar = [5, 2, 9, 1, 5, 6, 21, 45, 22, 99]
n = len(lista_ordenar)
for pasada in range(n - 1):
        for i in range(n - 1 - pasada):
                if lista_ordenar[i] > lista_ordenar[i + 1]:
                        lista_ordenar[i], lista_ordenar[i + 1] = \
                                lista_ordenar[i + 1], lista_ordenar[i] 