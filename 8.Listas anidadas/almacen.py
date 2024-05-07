productos = [
    ["botellas", 3, [1, 2]],
    ["frascos", 8, [1, 4]],
    ["fideos", 4, [2, 3]],
    ["leche", 6, [3, 4]]
]

def mostrar_menu():
    """
    Recibe: No recibe parámetros explícitos.
    Valida: No valida ningún dato.
    Retorna: No retorna ningún valor explícito, simplemente muestra el menú de opciones disponibles para el usuario.
    """
    print("\n--- Menú de opciones ---")
    print("1. Alta de productos")
    print("2. Baja de productos")
    print("3. Modificar productos")
    print("4. Listar productos")
    print("5. Listar productos ordenados por nombre")
    print("6. Salir")

def verificar_producto(nombre_producto:str):
    """
    Recibe: El nombre del producto a verificar.
    Valida: Verifica si el producto está presente en el almacén.
    Retorna: Un valor booleano (True/False) indicando si el producto está en el almacén.
    """
    for producto in productos:
        if nombre_producto == producto[0]:
            return True
    return False

def ingresar_producto_valido(mensaje: str):
    """
    Recibe: Un mensaje que se mostrará al usuario para solicitar el ingreso del producto.
    Valida: Verifica si el producto ingresado por el usuario está presente en el almacén.
    Retorna: El producto ingresado si está en el almacén, de lo contrario solicita nuevamente el ingreso del producto.
    """
    while True:
        nombre = input(mensaje)
        if verificar_producto(nombre):
            return nombre
        else:
            print("El producto ingresado no se encuentra en el almacén.")

def alta_producto():
    '''
    Recibe: No recibe parámetros explícitos.
    Valida: No valida datos directamente, pero verifica si la posición ingresada para el nuevo producto está ocupada.
    Retorna: No retorna ningún valor explícito, simplemente agrega el nuevo producto a la lista de productos.
        '''
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad inicial: "))
    
    # Solicitar la posición al usuario
    while True:
        fila = int(input("Ingrese la fila de ubicación: "))
        columna = int(input("Ingrese la columna de ubicación: "))
        
        # Verificar si la posición está ocupada
        ocupada = False
        for producto in productos:
            if producto[2] == [fila, columna]:
                ocupada = True
                break
        
        if ocupada:
            print(f"Error: La posición {fila, columna} ya está ocupada.")
        else:
            break
    
    productos.append([nombre, cantidad, [fila, columna]])
    print("Producto agregado correctamente.")

def baja_producto():
    '''
    Recibe: No recibe parámetros explícitos.
    Valida: Verifica si el nombre del producto ingresado por el usuario existe en el almacén.
    Retorna: No retorna ningún valor explícito, simplemente elimina el producto de la lista de productos si se encuentra.
    '''
    nombre = ingresar_producto_valido("Ingrese el nombre del producto a dar de baja: ")
    for i in range(len(productos)):
        if productos[i][0] == nombre:
            productos.pop(i)
            print("Producto dado de baja correctamente.")
            return

def modificar_producto():
    '''
    Recibe: No recibe parámetros explícitos.
    Valida: Verifica si el nombre del producto ingresado por el usuario existe en el almacén y valida la opción ingresada por el usuario (cantidad/posición).
    Retorna: No retorna ningún valor explícito, simplemente modifica la cantidad o la posición del producto en la lista de productos.
    '''
    nombre = ingresar_producto_valido("Ingrese el nombre del producto a modificar: ")
    for producto in productos:
        if producto[0] == nombre:
            while True:
                opcion = input("¿Qué desea modificar? (cantidad/posicion): ")
                if opcion == "cantidad":
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    producto[1] = nueva_cantidad
                    print("Cantidad modificada correctamente.")
                    break
                elif opcion == "posicion":
                    # Solicitar la nueva posición al usuario
                    while True:
                        nueva_fila = int(input("Ingrese la nueva fila de ubicación: "))
                        nueva_columna = int(input("Ingrese la nueva columna de ubicación: "))
                        
                        # Verificar si la nueva posición está ocupada
                        ocupada = False
                        for otro_producto in productos:
                            if otro_producto != producto and otro_producto[2] == [nueva_fila, nueva_columna]:
                                ocupada = True
                                break
                        
                        if ocupada:
                            print(f"Error: La posición {nueva_fila, nueva_columna} ya está ocupada.")
                        else:
                            producto[2] = [nueva_fila, nueva_columna]
                            print("Ubicación modificada correctamente.")
                            break
                    break
                else:
                    print("Opción inválida. Por favor, ingrese 'cantidad' o 'posicion'.")
            return

def listar_productos():
    '''
    Recibe: No recibe parámetros explícitos.
    Valida: No valida ningún dato.
    Retorna: No retorna ningún valor explícito, simplemente muestra la lista de productos en el almacén.
    '''
    for producto in productos:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicación: ({producto[2][0]}, {producto[2][1]})")

def listar_productos_ordenados():
    '''
    Recibe: No recibe parámetros explícitos.
    Valida: No valida ningún dato.
    Retorna: No retorna ningún valor explícito, simplemente ordena la lista de productos por nombre y luego la muestra.
    '''
    for i in range(len(productos)-1):
        for j in range(i+1, len(productos)):
            if(productos[i][0] > productos[j][0]):  #[0] porque quiero que ordene por nombre
                lista_aux = productos[i]
                productos[i] = productos[j]
                productos[j] = lista_aux

    for producto in productos:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicación: ({producto[2][0]}, {producto[2][1]})")
