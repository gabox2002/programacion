estanteria = [
    [["to12",65],["to16",86],["to20",65],["to25",45]],
    [["to30",68],["to35",73],["to40",85],["to45",89]],
    [["ta4",58],["ta5",48],["ta6",64],["ta7",96]],
    [["ta8",36],["ta10",72],["ta12",78],["ta14",71]]
]

def mostrar_menu():
    """
    Muestra el menú de opciones disponibles para el usuario.
    No recibe ningún parámetro.
    No valida ningún dato.
    No retorna ningún valor.
    """
    print("\nMenú de opciones:")
    print("1- Reponer mercadería (productos existentes)")
    print("2- Vender mercadería (producto existente, solo si alcanza el stock)")
    print("3- Listar inventario")
    print("4- Salir")

def verificar_producto(producto:str):
    """
    Recibe:  Una cadena que representa el nombre del producto a verificar.
    Valida:  Si el producto está presente en la estantería.
    Retorna: True si el producto está en la estantería
             False si no lo está.
    """
    for fila in estanteria:
        for cajon in fila:
            if cajon[0] == producto:
                return True
    return False

def ingresar_producto_valido(mensaje:str):
    """
    Recibe: El mensaje(str) que se mostrará al usuario para solicitar el ingreso del producto.
    Valida: Si el producto ingresado por el usuario está presente en la estantería.
    Retorna: El producto ingresado si está en la estantería, de lo contrario solicita nuevamente el ingreso.
    """
    while True:
        producto = input(mensaje)
        if verificar_producto(producto):
            return producto
        else:
            print("El producto ingresado no se encuentra en la estantería.")

def reponer_mercaderia(producto:str, cantidad:int):
    """
    Recibe:  Una cadena(producto) y un entero(cantidad), ingresado por el usuario
    Valida:  Si el producto está presente en la estantería usando la función verificar_producto.
    Retorna: True si la reposición fue exitosa
             False si el producto no está en la estantería
    """
    for fila in estanteria:
        for cajon in fila:
            if cajon[0] == producto:
                cajon[1] += cantidad
                print("Reposición exitosa.")
                return True
    print("El producto ingresado no se encuentra en la estantería.")
    return False
    
def vender_mercaderia(producto:str, cantidad:int):
    """
    Recibe: producto y cantidad, ingresado por el usuario
    Valida: Si hay suficiente stock para realizar la venta
    Retorna: True si la venta fue realizada(si hay suficiente stock para la venta)
             False si no hay suficiente stock.
    """
    for fila in estanteria:
        for cajon in fila:
            if cajon[0] == producto:
                while cajon[1] < cantidad:
                    print(f"No hay suficiente stock. Hay disponible {cajon[1]}u del producto {cajon[0]}.")
                    # Solicitar al usuario ingresar nuevamente la cantidad
                    cantidad = int(input("Ingrese la cantidad a vender: "))
                    cajon[1] -= cantidad
                    print("Venta realizada.")
                    return True
    print("El producto ingresado no se encuentra en la estantería.")
    return False

def listar_inventario(estanteria:list):
    """
    Imprime el inventario completo de la estantería
    Recibe: estanteria (lista de listas)
    No valida ningún dato. No retorna ningún valor.
    """
    for fila in estanteria:
        for cajon in fila:
            print(f"Producto: {cajon[0]}, Stock: {cajon[1]}")

def salir():
    """
    Imprime un mensaje de despedida
    No recibe ningún parámetro. 
    No valida ningún dato. No retorna ningún valor.
    """
    print("Saliendo del programa...")
