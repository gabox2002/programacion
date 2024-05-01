'''
Ejercicio 5: 
Crear una función lambda que realice un 10% de descuento en el
importe recibido.
'''

aplicar_descuento = lambda importe: importe * 0.9

print("El importe con descuento del 10% es:", int(aplicar_descuento(100)))
