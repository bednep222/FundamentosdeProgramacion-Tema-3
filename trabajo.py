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
        