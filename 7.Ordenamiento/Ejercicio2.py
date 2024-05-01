'''
Ejercicio 2: 
Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente.
'''
# Listas de nombres y puntos
nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [     100,                   98,             56,         25,        87,        38,         64,        42,       28,          91,           66,          35,            49,            57,         98]

def ordenar_por_nombre(nombres:list, puntos:list)->list:
    """
    Recibe: nombres (list): Lista de nombres.
            puntos (list): Lista de puntos.
    Valida: Que las listas 'nombres' y 'puntos' tengan la misma longitud y que contengan valores correspondientes uno a uno.
    Retorna: Una lista ordenada por nombre de manera ascendente junto con sus puntos respectivos.
    """
    # Ordenamiento por nombre ascendente y puntos descendente
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if nombres[i] > nombres[j]:
                # Si los nombres son diferentes, intercambiar
                auxn = nombres[i]
                auxp = puntos[i]

                nombres[i] = nombres[j]
                puntos[i] = puntos[j]

                nombres[j] = auxn
                puntos[j] = auxp
            elif nombres[i] == nombres[j]:
                # Si los nombres son iguales, ordenar por puntos de manera descendente
                if puntos[i] < puntos[j]:
                    auxp = puntos[i]

                    puntos[i] = puntos[j]
                    puntos[j] = auxp

    return nombres, puntos

# Llamada a la función para ordenar por nombre ascendente y puntos descendente
ordenar_por_nombre(nombres, puntos)

# Impresión de las listas ordenadas
print("Nombres ordenados:", nombres)
print("Puntos:", puntos)
