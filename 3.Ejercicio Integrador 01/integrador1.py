'''
Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.


Ejemplo de la consola:
El mas caro de los barbijkos tiene una cantidad de: 100unidades y es fabricado por: L1
El item con mas unidades es: L1 y es: 100
La cantidad de jabones es: 320
Gracias por usar el programa
'''

contador_producto = 0
contador_barbijo = 0
contador_jabon = 0
contador_alcohol = 0
contador_mascara = 0
precio_mas_caro_barbijo = 0
cantidad_mas_caro_barbijo = 0
fabricante_mas_caro_barbijo = ""
cantidad_mas_unidades = 0
fabricante_mas_unidades = ""
cantidad_total_jabon = 0

for i in range(5):   
    tipo_producto = input("Ingrese el tipo de producto (barbijo, jabón, alcohol o mascarilla): ").lower()
    while tipo_producto != "barbijo" and tipo_producto != "jabón" and tipo_producto != "alcohol" and tipo_producto != "mascarilla":
        tipo_producto = input("Por favor, ingrese un tipo de producto válido (barbijo, jabón, alcohol o mascarilla): ").lower()

    precio_producto = float(input("Ingrese el precio del producto: "))
    while precio_producto < 0:
        precio_producto = float(input("Por favor, ingrese un precio válido mayor a cero: "))

    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
    while cantidad_unidades < 0:
        cantidad_unidades = int(input("Por favor, ingrese una cantidad positiva: "))
    
    marca_producto = input("Ingrese la marca del producto: ")
    fabricante_producto = input("Ingrese el nombre del fabricante del producto: ")

    if tipo_producto == "barbijo":
        contador_barbijo += 1
        if precio_producto > precio_mas_caro_barbijo:
            precio_mas_caro_barbijo = precio_producto
            cantidad_mas_caro_barbijo = cantidad_unidades
            fabricante_mas_caro_barbijo = fabricante_producto
    elif tipo_producto == "jabón":
        contador_jabon += 1
        cantidad_total_jabon += cantidad_unidades
    elif tipo_producto == "mascarilla":
        contador_mascara += 1
    else:
        contador_alcohol += 1

    if cantidad_unidades > cantidad_mas_unidades:
        cantidad_mas_unidades = cantidad_unidades
        tipo_mas_unidades = tipo_producto

print("El más caro de los barbijos tiene una cantidad de:", cantidad_mas_caro_barbijo, "unidades y es fabricado por:", fabricante_mas_caro_barbijo)
print("El item con más unidades es", tipo_mas_unidades, "y es:", cantidad_mas_unidades)
print("La cantidad de jabones es", cantidad_total_jabon)
print("Gracias por usar el programa")