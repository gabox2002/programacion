'''
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = [    "m",    "m",   "f",   "m",  "f"]
nota = [     6,      8,    10,     8,    5]
'''

# Listas para almacenar los datos de los alumnos
nombres = []
sexo = []
nota = []

# Función de validación para el sexo
def validar_sexo(s):
    return s == 'f' or s == 'm'

# Función de validación para la nota
def validar_nota(n):
    return 0 <= n <= 10

# Solicitar datos de los alumnos
for i in range(5):
    nombres.append(input("Ingrese el nombre del alumno: "))
    
    # Validar el sexo
    s = input("Ingrese el sexo del alumno (f/m): ").lower()
    while validar_sexo(s) == False:  
        print("Error: el sexo debe ser 'f' o 'm'.")
        s = input("Ingrese el sexo del alumno (f/m): ").lower()
    sexo.append(s)
    
    # Validar la nota
    while True:
        n = input("Ingrese la nota del alumno: ")
        if n.isdigit():
            n = float(n)
            if 0 < n and n <= 10:  
                nota.append(n)
                break
            else:
                print("Error: la nota debe estar entre 0 y 10.")
        else:
            print("Error: ingrese un número válido entre 0 y 10.")

# Encontrar el hombre con la nota más baja
if 'm' in sexo:
    nota_baja_hombre = nota[0]  # Suponemos que la primera nota es la más baja
    nombre_hombre_nota_baja = nombres[0]  # Suponemos que el primer nombre corresponde a la nota más baja

    for i in range(1, len(nota)):
        if sexo[i] == 'm' and nota[i] < nota_baja_hombre:
            nota_baja_hombre = nota[i]
            nombre_hombre_nota_baja = nombres[i]

    print(f"El hombre con la nota más baja es {nombre_hombre_nota_baja} con nota {nota_baja_hombre}.")
else:
    print("No se encontraron hombres en la lista.")

# Calcular el promedio de notas de las mujeres
notas_mujeres = []
for i in range(len(sexo)):
    if sexo[i] == 'f':
        notas_mujeres.append(nota[i])

if notas_mujeres:
    promedio_notas_mujeres = sum(notas_mujeres) / len(notas_mujeres)
    print(f"El promedio de notas de las mujeres es: {promedio_notas_mujeres}")
else:
    print("No se encontraron mujeres en la lista.")

