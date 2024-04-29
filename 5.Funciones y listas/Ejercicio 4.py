'''
Ejercicio 4: 
Desarrollar una función que reciba por parámetro, una lista de números
y un número especificado. La misma debe buscar el número especificado en la lista
y retornar “True” si existe.

'''
def buscar_numero(lista, numero_especificado):
    """
    Recibe: Una lista de números y un número especificado a buscar.
    Valida: No realiza validación específica.
    Retorna: True si el número especificado está en la lista, False de lo contrario.
    """
    if numero_especificado in lista:
        return True
    else:
        return False

# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
numero_buscado = 10
resultado = buscar_numero(numeros, numero_buscado)
print(resultado)  
