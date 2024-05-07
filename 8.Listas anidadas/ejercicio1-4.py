from almacen import *

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_producto()
        elif opcion == "2":
            baja_producto()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            listar_productos()
        elif opcion == "5":
            listar_productos_ordenados()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida del 1 al 6")

main()