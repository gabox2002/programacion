#Ejercicio 3
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

suma_positivos = 0
producto_negativos = 1
cantidad_pares = 0
cantidad_impares = 0
mayor_par = 0  
menor_numero_flag = 0  
primer_numero_flag = True  # Bandera para el primer número ingresado

for contador in range(5):
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    
    if numero != 0:
        if primer_numero_flag:  # Verificar si es el primer número ingresado
            menor_numero_flag = numero
            primer_numero_flag = False
        
        if numero > 0:
            suma_positivos += numero
        elif numero < 0:
            producto_negativos *= numero
        
        if numero % 2 == 0:
            cantidad_pares += 1
            if numero > mayor_par:
                mayor_par = numero
        else:
            cantidad_impares += 1
        
        if numero < menor_numero_flag:  
            menor_numero_flag = numero
    else:
        print("Por favor, ingrese un número distinto de cero.")

print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")
# Imprimir el mayor número par, si es que hay números pares
if cantidad_pares > 0:
    print(f"De los pares el mayor número ingresado es: {mayor_par}")
print(f"El menor número ingresado es: {menor_numero_flag}")
print(f"Suma de los números positivos: {suma_positivos}")
print(f"Producto de los números negativos: {producto_negativos}")

