'''
Ejercicio 7:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares.
'''

numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

print("Los números pares son:")
for numero in numeros:
    if numero % 2 == 0:  # Verificar si el número es par
        print(numero)
