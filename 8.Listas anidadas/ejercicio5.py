from ferreteria import *

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = ingresar_producto_valido("Ingrese el producto a reponer: ")
            cantidad = int(input("Ingrese la cantidad a reponer: "))
            reponer_mercaderia(producto, cantidad)

        elif opcion == "2":
            producto = ingresar_producto_valido("Ingrese el producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            vender_mercaderia(producto, cantidad)

        elif opcion == "3":
            listar_inventario(estanteria)

        elif opcion == "4":
            salir()
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida del 1 al 4")

main()
