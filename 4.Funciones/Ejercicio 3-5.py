'''
Ejercicio 3-5: 
Realizar un programa en donde se puedan utilizar los prototipos de la
función Restar en sus 4 combinaciones.
- Restar1(int, int)->int:
- Restar2()->int:
- Restar3(int, int):
- Restar4():
'''

def Restar1(a: int, b: int) -> int:
    """
    Recibe: Dos números enteros.
    Valida: No realiza validación específica.
    Retorna: La resta de los dos números enteros.
    """
    return a - b

def Restar2() -> int:
    """
    Recibe: No recibe ningún parámetro.
    Valida: No realiza validación específica.
    Retorna: La resta de dos números enteros ingresados por el usuario.
    """
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1 - num2

def Restar3(a: int, b: int):
    """
    Recibe: Dos números enteros.
    Valida: No realiza validación específica.
    Retorna: Muestra la resta de los dos números por pantalla.
    """
    print("La resta3 de", a, "y", b, "es:", a - b)

def Restar4():
    """
    Recibe: No recibe ningún parámetro.
    Valida: No realiza validación específica.
    Retorna: Muestra la resta de dos números ingresados por el usuario por pantalla.
    """
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La resta4 de", num1, "y", num2, "es:", num1 - num2)

# Ejemplo de uso de las funciones
print("La resta1 es:", Restar1(5, 3))
print("La resta2 es:", Restar2())
Restar3(10, 7)
Restar4()
