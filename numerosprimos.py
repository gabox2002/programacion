'''
resolver con funciones recursivas
para calcular numeros primos'''

def primo(num:int, divisor:int)->bool:
    '''
    Recibe: dos argumentos n que es el numero a verificar y divisor si es divisible por él
    Válida: si el numero es primo utilizando enfoque recursivo
    Retorna: devuelve True si el numero es primo y False si no lo es
    '''
    if divisor == 1:
        return True
    elif num % divisor == 0:
        return False
    else:
        return primo(num, divisor - 1)

numero = int(input("Ingresa un número entero positivo: "))

if numero <= 1:
    print(numero, "no es primo")
elif primo(numero, numero - 1):
    print(numero, "es primo")
else:
    print(numero, "no es primo")