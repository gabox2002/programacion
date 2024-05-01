'''
Ejercicio 3: 
Crear una función lambda que indique si el número recibido es par o
impar.
'''

es_par = lambda numero: "Par" if numero % 2 == 0 else "Impar"

print("El número es:", es_par(3))