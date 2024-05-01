'''
Ejercicio 1: 
Crear una función lambda que incremente un 10% en el sueldo recibido.
'''

incrementar_sueldo = lambda sueldo: sueldo * 1.10

#nuevo_sueldo = "{:.2f}".format((incrementar_sueldo(sueldo_actual))) #para dos decimales

print(f"El nuevo sueldo después del aumento del 10% es: {int(incrementar_sueldo(100))}")
