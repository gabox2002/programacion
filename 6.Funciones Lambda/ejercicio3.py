'''
Ejercicio 3: 
Crear una función lambda que indique si el número recibido es par o
impar.
'''

es_par = lambda numero: "Par" if numero % 2 == 0 else "Impar"

numero = 4
resultado = es_par(numero)
print("El número es:", resultado)