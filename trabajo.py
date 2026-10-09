 # Etapa 3: Operaciones sobre listas (con funciones y return)
lista = [10, 20, 30, 40, 50]
print("Lista inicial:", lista)

def insertar_elemento(lista):
    """Inserta un valor al final y retorna la lista."""
    valor = int(input("Ingrese el valor a insertar: "))
    lista.append(valor)
    return lista

def eliminar_elemento(lista):
    """Elimina por posición (desde 1) y retorna la lista."""
    posicion = int(input("Ingrese la posición a eliminar: "))
    if posicion >= 1 and posicion <= len(lista):
        lista.pop(posicion - 1)
    else:
        print("Posición no válida")
    return lista

def buscar_elemento(lista):
    """Busca un valor y retorna la posición (desde 1) o -1 si no está."""
    valor = int(input("Ingrese el valor a buscar: "))
    for i in range(len(lista)):
        if lista[i] == valor:
            return i + 1
    return -1

def mostrar_lista(lista):
    """Retorna la lista para mostrarla."""
    return lista

seguir = True
while seguir == True:
    print("\n1. Insertar un elemento en la lista")
    print("2. Eliminar un elemento de la lista")
    print("3. Buscar un elemento en la lista")
    print("4. Mostrar la lista actualizada")
    print("5. Salir")
    opciones = int(input("Ingrese una opción (1-5): "))

    if opciones == 1:
        lista = insertar_elemento(lista)
        print("Lista después de insertar:", lista)

    elif opciones == 2:
        lista = eliminar_elemento(lista)
        print("Lista después de eliminar:", lista)

    elif opciones == 3:
        posicion = buscar_elemento(lista)
        if posicion != -1:
            print("El valor se encuentra en la posición:", posicion)
        else:
            print("El valor no se encuentra en la lista.")

    elif opciones == 4:
        print("Lista actualizada:", mostrar_lista(lista))

    elif opciones == 5:
        seguir = False
        print("Fin del programa")

    else:
        print("Opción inválida. Ingrese un número del 1 al 5.") 