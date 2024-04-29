'''
Ejercicio 3-2: 
Crear una función que pida el ingreso de un número y lo retorne.
'''
def ingresar_numero():
    """
    Recibe: No recibe ningún parámetro.
    Valida: No realiza validación específica.
    Retorna: El número ingresado por el usuario como una cadena de caracteres.
    """
    numero = input("Ingrese un número: ")
    return numero

# Ejemplo de uso
numero_ingresado = ingresar_numero()
print("El número ingresado es:", numero_ingresado)

# # del Ejercicio 3.4
# def ingresar_numero(desde, hasta):
#     """
#     Recibe: Los límites inferior y superior del rango permitido.
#     Valida: Si el número ingresado por el usuario está dentro del rango especificado.
#     Retorna: El número ingresado por el usuario.
#     """
#     while True:
#         numero = int(input(f"Ingrese un número entre {desde} y {hasta}: "))
#         if numero >= desde and numero <= hasta:
#             return numero
#         else:
#             print("El número no está dentro del rango especificado. Intente nuevamente.")

# # Ejemplo de uso
# limite_desde = 1
# limite_hasta = 10
# numero_ingresado = ingresar_numero(limite_desde, limite_hasta)
# print("El número ingresado es:", numero_ingresado)
