'''
Ejercicio 3-7: 
Realizar un programa que: asigne a las variables numero1 y numero2
los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
la operación de dichos valores a través de una función. Mostrar el resultado por
pantalla.
'''

def realizarOperacion(numero1, numero2, operacion):
    """
    Recibe: Dos números y una cadena que representa la operación ('s' para sumar, 'r' para restar).
    Valida: Si la operación es válida ('s' o 'r').
    Retorna: El resultado de la operación.
    """
    if operacion == 's':
        return numero1 + numero2
    elif operacion == 'r':
        return numero1 - numero2
    else:
        return "Operación no válida."

def solicitarNumero():
    """
    Recibe: No recibe ningún parámetro.
    Valida: Si el número ingresado por el usuario está dentro del rango especificado (entre 10 y 100).
    Retorna: El número ingresado por el usuario.
    """
    while True:
        numero = int(input("Ingrese un número entre 10 y 100: "))
        if 10 <= numero <= 100:
            return numero
        else:
            print("El número ingresado no está dentro del rango permitido. Intente nuevamente.")

# Programa principal
numero1 = solicitarNumero()
numero2 = solicitarNumero()

operacion = input("Ingrese la operación a realizar ('s' para sumar, 'r' para restar): ")

if operacion == 's' or operacion == 'r':
    resultado = realizarOperacion(numero1, numero2, operacion)
    print("El resultado de la operación es:", resultado)
else:
    print("Operación no válida.")
