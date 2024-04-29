'''
PEDIR DOS NUMEROS Y MOSTRAR LA SUMA
1)FUNCION SIN PARAMETROS NI RETORNOS
2)FUNCION SIN PARAMETROS CON RETORNO
3)FUNCION CON PARAMETROS SIN RETORNO
4)FUNCION CON PARAMETROS CON RETORNO
'''

def sumar_sin_parametro_sin_retorno():
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    suma = num1 + num2
    print("La suma es:" , suma)

sumar_sin_parametro_sin_retorno()


def suma_sin_parametro_con_retorno():
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    suma = num1 + num2
    return suma

resultado = suma_sin_parametro_con_retorno()
print("La suma es:", resultado)



def suma_con_parametros_sin_retorno(num1, num2):
    suma = num1 + num2
    print("La suma es:", suma)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma_con_parametros_sin_retorno(num1, num2)



def suma_con_parametros_con_retorno(num1:int, num2:int)-> int:
    suma = num1 + num2
    return suma

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = suma_con_parametros_con_retorno(num1, num2)
print("La suma es:", resultado)