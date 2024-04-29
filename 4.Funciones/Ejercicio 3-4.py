'''
Ejercicio 3-4: 
Especializar la función del punto 3.1 y 3.2 para que valide el número en
un rango determinado pasado por parámetro “desde”-“hasta”.
'''
# del 3.1
def mostrar_numero(numero, desde, hasta):
    """
    Recibe: Un número y los límites inferior y superior del rango permitido.
    Valida: Si el número está dentro del rango especificado.
    Retorna: El número si está dentro del rango; si no, no retorna explícitamente nada.    
    """
    if numero >= desde and numero <= hasta:
        print(numero)
    else:
        print("El número no está dentro del rango especificado.")
        
# Ejemplo de uso 
numero = 4
limite_desde = 1
limite_hasta = 10
mostrar_numero(numero, limite_desde, limite_hasta)

# del 3.2
def ingresar_numero(desde, hasta):
    """
    Recibe: Los límites inferior y superior del rango permitido.
    Valida: Si el número ingresado por el usuario está dentro del rango especificado.
    Retorna: El número ingresado por el usuario.
    """
    while True:
        numero = int(input(f"Ingrese un número entre {desde} y {hasta}: "))
        if numero >= desde and numero <= hasta:
            return numero
        else:
            print("El número no está dentro del rango especificado. Intente nuevamente.")

# Ejemplo de uso 
limite_desde = 1
limite_hasta = 10
numero_ingresado = ingresar_numero(limite_desde, limite_hasta)
print("El número ingresado es:", numero_ingresado)