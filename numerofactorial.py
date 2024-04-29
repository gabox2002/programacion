'''
resolver con funciones recursivas
- permutacion
'''
def factorial(num)->int:
    if num == 0: 
        return 1
    else:
        return num * factorial(num - 1)  

numero = 0
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")