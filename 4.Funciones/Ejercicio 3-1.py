'''
Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
como parámetro.
'''

def mostrar_numero(numero:int):
    """
    Recibe: un número como parámetro
    Valida: No realiza validación específica.
    Retorna: el numero por pantalla
    """
    print(numero)
    
# Ejemplo de uso
numero = 12
mostrar_numero(numero)


# del ejercicio 3.4
# def mostrar_numero(numero, desde, hasta):
#     """
#     Recibe: Un número y los límites inferior y superior del rango permitido.
#     Valida: Si el número está dentro del rango especificado.
#     Retorna: El número si está dentro del rango; si no, no retorna explícitamente nada.    
#     """
#         if numero >= desde and numero <= hasta:
#         print(numero)
#     else:
#         print("El número no está dentro del rango especificado.")

# # Ejemplo de uso
# numero = 4
# limite_desde = 1
# limite_hasta = 10
# mostrar_numero(numero, limite_desde, limite_hasta)