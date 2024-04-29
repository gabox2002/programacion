'''
Ejercicio 3-6: 
Realizar un programa que: asigne a la variable numero1 un valor
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
por pantalla. Atención: pueden reutilizarse funciones ya creadas.
'''

def realizarDescuento(numero):
    """
    Recibe: Un número.
    Valida: No realiza validación específica.
    Retorna: El número con un descuento del 5% aplicado.
    """
    descuento = numero * 0.05
    return numero - descuento

def solicitarNumero():
    """
    Recibe: No recibe ningún parámetro.
    Valida: Si el número ingresado por el usuario está dentro del rango especificado (entre 10 y 100).
    Retorna: El número ingresado por el usuario.
    """
    while True:
        numero = int(input("Ingrese un número entre 10 y 100: "))
        if numero >= 10 and numero <= 100:
            return numero
        else:
            print("El número ingresado no está dentro del rango permitido. Intente nuevamente.")

# Programa principal
numero1 = solicitarNumero()
numero1_con_descuento = realizarDescuento(numero1)
print("El número", numero1, "con un descuento del 5% es:", numero1_con_descuento)
