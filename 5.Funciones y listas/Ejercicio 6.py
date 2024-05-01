'''
Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
listas_personas.py. Importar los nombres a una lista. Realizar una función que
muestre los mismos.
'''

from listas_personas import nombres

def mostrar_nombres():
    """
    Función que muestra los nombres de las personas. no recibe, no valida ni retorna algun valor
    """
    print("Nombres de las personas:")

    lista_nombres = nombres
    
    for i in range(len(lista_nombres)):
        print(lista_nombres[i])

# Llama a la función para mostrar los nombres de las personas
mostrar_nombres()