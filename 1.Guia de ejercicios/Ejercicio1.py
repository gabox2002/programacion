'''
ejercicio 1: Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
'''
nombre = input ("Ingrese su nombre\n")
sueldo = input ("Ingrese su sueldo\n")

sueldo_float = float(sueldo)
sueldo_aumentado = sueldo_float *1.10

print ("El sueldo aumentado es: ", sueldo_aumentado)
