'''
Ejercicio 2: 
Crear una función lambda que informe si una persona es mayor (mayor a
17 años) o menor.
'''

es_mayor_de_edad = lambda edad: "Mayor de edad" if edad > 17 else "Menor de edad"

edad_persona = 16
estado = es_mayor_de_edad(edad_persona)
print("La persona es:", estado)

