'''
Ejercicio 2: 
Desarrollar una función que inicialice una lista de 10 números en 0, pida
posición y número a guardar al usuario, lo guarde en una lista en la posición
solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
función y mostrar por pantalla el retorno.
'''

def ingresar_numero(lista):
    """
    Recibe: Una lista de números.
    Valida: Si la posición ingresada por el usuario es válida.
    Retorna: La lista con el número ingresado por el usuario en la posición especificada.
    """
    posicion = int(input("Ingrese la posición donde desea guardar el número (0-9): "))
    while posicion < 0 or posicion > 9:
        print("La posición debe estar entre 0 y 9. Intente nuevamente.")
        posicion = int(input("Ingrese la posición donde desea guardar el número (0-9): "))
    
    numero = int(input(f"Ingrese el número que desea guardar en la posición {posicion}: "))
    lista[posicion] = numero
    return lista

# Programa principal
lista_numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Inicializa una lista con 10 elementos en 0

lista_modificada = ingresar_numero(lista_numeros)
print("La lista modificada es:", lista_modificada)