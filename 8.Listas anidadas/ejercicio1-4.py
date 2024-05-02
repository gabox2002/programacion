from almacen import *

alta_realizada = False
productos = []

while True:
    print("\nMenú de opciones:")
    print("1- Alta de productos")
    print("2- Baja de productos")
    print("3- Modificar productos")
    print("4- Listar productos")
    print("5- Lista de productos ordenado por nombre")
    print("6- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        productos = alta_de_productos(productos)
        alta_realizada = True
    elif opcion == "2":
        if alta_realizada:
            productos = baja_de_productos(productos)
        else:
            print("Primero debe realizar un alta de productos.")
    elif opcion == "3":
        if alta_realizada:
            productos = modificar_productos(productos)
        else:
            print("Primero debe realizar un alta de productos.")
    elif opcion == "4":
        listar_productos(productos)
    elif opcion == "5":
        lista_productos_ordenados(productos)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Saliendo del programa...")
        break
