'''
Ejercicio 3: 
Desarrollar una función que pida 10 números dentro de un rango especificado, validar los números solicitados dentro de ese rango, guardar en una lista y retornarla. El programa principal debe invocar a la función y mostrar por pantalla el retorno.
'''
#Ejercicio de carga secuencial

def pedir_numeros():
    """
    Recibe: No recibe parámetros.
    Valida: Los números ingresados deben estar dentro del rango especificado.
    Retorna: Una lista que contiene los 10 números ingresados por el usuario.
    """
    numeros = []
    for i in range(10):
        numero = int(input(f"Ingrese el número {i+1} dentro del rango (-100, 100): "))
        if numero < -100 or numero > 100:
            print("El número debe estar dentro del rango (-100, 100). Intente nuevamente.")
            numero = int(input(f"Ingrese el número {i+1} dentro del rango (-100, 100): "))
        numeros.append(numero)
    return numeros

# Programa principal
lista_numeros = pedir_numeros()
print("Los números ingresados son:", lista_numeros)

