'''
Ejercicio 1: 
Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.
'''
def pedir_nombres():
    """
    Recibe: No recibe parámetros.
    Valida: No realiza validación específica.
    Retorna: Una lista que contiene los 10 nombres ingresados por el usuario.
    """
    nombres = []
    for i in range(10):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    return nombres

# Programa principal
lista_nombres = pedir_nombres()
print("Los nombres ingresados son:", lista_nombres)