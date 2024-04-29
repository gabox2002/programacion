'''
Ejercicio 1: 
Dadas las siguientes listas:
Nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.
'''
# Listas de nombres y edades
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,       45,     34,     23,      46,        23,       45,     67,      37,      68,       25,        55,        45,       27,      43]

def ordenar_por_nombre_ascendente(nombres:list, edades:list)->list:
    """
    Recibe: nombres (list): Lista de nombres.
            edades (list): Lista de edades.
    Valida: Que las listas 'nombres' y 'edades' tengan la misma longitud y que contengan valores correspondientes uno a uno.
    Retorna: Una lista ordenada por nombre de manera ascendente junto con sus edades respectivas.
    """
    # Ordenamiento por nombre ascendente
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if nombres[i] > nombres[j]:
                auxn = nombres[i]
                auxe = edades [i]

                nombres[i] = nombres[j]
                edades[i] = edades[j]

                nombres[j] = auxn
                edades[j] = auxe

            if nombres[i] == nombres[j]:
                if edades[i] > edades[j]:
                    auxn = nombres[i]
                    auxe = edades [i]

                    nombres[i] = nombres[j]
                    edades[i] = edades[j]

                    nombres[j] = auxn
                    edades[j] = auxe
    return nombres, edades

# Llamada a la función para ordenar por nombre ascendente
ordenar_por_nombre_ascendente(nombres, edades)

# Impresión de las listas ordenadas
print("Nombres ordenados:", nombres)
print("Edades:", edades)