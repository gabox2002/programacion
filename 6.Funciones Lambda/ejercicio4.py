'''
Ejercicio 4: 
Crear una función lambda que indique si el número recibido es positivo o
negativo.
'''

es_positivo_o_negativo = lambda numero: "Positivo" if numero > 0 else "Negativo" if numero < 0 else "Cero"

numero = -1
resultado = es_positivo_o_negativo(numero)
print("El número es:", resultado)
