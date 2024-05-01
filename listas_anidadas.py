#Lista de alumnos con sus materias
alumno1 = ["Juan", ["Matematicas", "Historia"]]
alumno2 = ["Maria", ["Fisica", "Literatura"]]
alumno3 = ["Pedro", ["Quimica", "Geografia"]]

#Listas anidadas que contiene los alumnos
listas_alumnos = [alumno1, alumno2, alumno3]

#imprimir informacion de cada alumno y sus materias
# for alumno in listas_alumnos:
#     print("Alumno :", alumno[0])
#     print("Materias :", alumno[1])

#Actualizar Historia por Sociales
print("Imprimo de a uno")
print(listas_alumnos[0][0])
print(listas_alumnos[0][1])
print(listas_alumnos[0][1][0])
print(listas_alumnos[0][1][1])


listas_alumnos[0][1][1] = "Sociales"
print("Imprimo a Juan")
print(listas_alumnos[0][0])
print(listas_alumnos[0][1])
print(listas_alumnos[0][1][0])
print(listas_alumnos[0][1][1])