'''
Ejercicio 5: Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las
personas de menor edad (puede ser más de una) y las retorne. El programa
principal deberá mostrar nombre y edad de los menores.
'''

Nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

def buscar_personas_menores(edades):
    '''
    Recibe una lista de edades
    Valida si hay personas de menor de edad
    Retorna una lista que contiene nombre y la edad de las personas de menor edad
    '''
    menor_edad = edades[0]
    personas_menores = []
    
    for edad in edades:
        if edad < menor_edad:
            menor_edad = edad
    
    for i in range(len(edades)):
        if edades[i] == menor_edad:
            personas_menores.append(i)

    return personas_menores

personas_menores = buscar_personas_menores(edades)

print("Contenido de lista personas menores: ")
for i in range(len(personas_menores)):
       print (Nombres[personas_menores[i]], "de", edades[personas_menores[i]], "años")
