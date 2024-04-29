'''
Ejercicio 3-3: 
Crear una función que permita determinar si un número es par o no. La
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
programa principal realizando la invocación o llamada.
'''

def es_par(numero):
    """
    Recibe: Un número entero.
    Valida: No realiza validación específica.
    Retorna: True si el número es par, False si es impar.
    """
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número entero: "))

if es_par(numero):
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")
