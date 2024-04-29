'''
Ejercicio 3: 
Dadas las siguientes listas:
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia","Soledad", "Mario", "María"]
Apellidos = [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, debe ordenar por nota de manera descendente.
'''

# Listas de estudiantes, apellidos y notas
estudiantes = ["Ana",   "Luis",    "Juan",     "Sol", "Roberto",  "Sonia",  "María", "Sofia",  "Maria",  "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa",  "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade",   "Loza",  "Antares", "Roca",  "Perez"]
notas = [       8,         4,         9,         10,        8,        6,        4,       8,        7,        5,        6,        7,         10,       4,      8]

def ordenar_estudiantes(estudiantes:list, apellidos:list, notas:list)->list:
    """
    Recibe: estudiantes (list): Lista de nombres de estudiantes.
            apellidos (list): Lista de apellidos de estudiantes.
            notas (list): Lista de notas de estudiantes.
    Valida: Que las listas 'estudiantes', 'apellidos' y 'notas' tengan la misma longitud y que contengan valores correspondientes uno a uno.
    Retorna:  Una lista ordenada por apellido de manera ascendente, en caso de apellidos iguales, ordena por nombre de manera ascendente y en caso de nombres iguales, ordena por nota de manera descendente.
    """

    for i in range(len(estudiantes)-1):
        for j in range(i+1, len(estudiantes)):
            # Comparación de apellidos orden ascendente
            if apellidos[i] > apellidos[j]:
                auxe = estudiantes[i]
                auxa = apellidos[i]
                auxn = notas[i]

                estudiantes[i] = estudiantes[j]
                apellidos[i] = apellidos[j]
                notas[i] = notas[j]

                estudiantes[j] = auxe
                apellidos[j] = auxa
                notas[j] = auxn
            # Si los apellidos son iguales, comparación de nombres ascendente
            elif apellidos[i] == apellidos[j]:
                if estudiantes[i] > estudiantes[j]:
                    auxe = estudiantes[i]
                    auxa = apellidos[i]
                    auxn = notas[i]

                    estudiantes[i] = estudiantes[j]
                    apellidos[i] = apellidos[j]
                    notas[i] = notas[j]

                    estudiantes[j] = auxe
                    apellidos[j] = auxa
                    notas[j] = auxn
                # Si los nombres también son iguales, comparación de notas descendente
                elif estudiantes[i] == estudiantes[j]:
                    if notas[i] < notas[j]:
                        auxe = estudiantes[i]
                        auxa = apellidos[i]
                        auxn = notas[i]

                        estudiantes[i] = estudiantes[j]
                        apellidos[i] = apellidos[j]
                        notas[i] = notas[j]

                        estudiantes[j] = auxe
                        apellidos[j] = auxa
                        notas[j] = auxn
    return apellidos, estudiantes, notas

# Llamada a la función para ordenar estudiantes, apellidos y notas
ordenar_estudiantes(estudiantes, apellidos, notas)

# Impresión de los estudiantes ordenados
print("Apellidos ordenados:", apellidos)
print("Nombres:", estudiantes)
print("Nota:", notas)