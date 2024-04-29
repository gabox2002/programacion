'''
Ejercicio 1: 
Crear una función lambda que incremente un 10% en el sueldo recibido.
'''

incrementar_sueldo = lambda sueldo: sueldo * 1.10

sueldo_actual = 100
nuevo_sueldo = incrementar_sueldo(sueldo_actual)
#nuevo_sueldo = "{:.2f}".format((incrementar_sueldo(sueldo_actual))) #para dos decimales

print("El nuevo sueldo después del aumento del 10% es:", nuevo_sueldo)
