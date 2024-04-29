'''
Ejercicio 5: 
Crear una función lambda que realice un 10% de descuento en el
importe recibido.
'''

aplicar_descuento = lambda importe: importe * 0.9

importe_original = 100
importe_con_descuento = aplicar_descuento(importe_original)
print("El importe con descuento del 10% es:", importe_con_descuento)
