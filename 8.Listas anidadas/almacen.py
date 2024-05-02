#1
def alta_de_productos(productos):
    '''
    Recibe: La lista de productos.
    Valida: Verifica que la fila y columna estén dentro del rango permitido y que la ubicación no esté ocupada por otro producto.
    Retorna: La lista actualizada de productos después de agregar un nuevo producto.
    '''
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))

    while True:
        nueva_fila = int(input("Ingrese la fila de la góndola (1, 2 o 3): "))
        nueva_columna = int(input("Ingrese la columna de la góndola (1, 2, 3 o 4): "))

        # Verificamos que la fila y columna estén dentro del rango permitido
        validar_ubicacion = lambda fila, columna: 1 <= fila <= 3 and 1 <= columna <= 4
        if validar_ubicacion(nueva_fila, nueva_columna):
            # Verificamos si la fila y columna ya están ocupadas por otro producto
            ubicacion_ocupada = False
            for producto in productos:
                if producto[2][0] == nueva_fila and producto[2][1] == nueva_columna:
                    ubicacion_ocupada = True
                    break

            if ubicacion_ocupada:
                print("Ya hay un producto en esta ubicación. Elija una ubicación diferente.")
            else:
                # Si la ubicación está disponible, agregamos el producto a la lista
                producto = [nombre, cantidad, [nueva_fila, nueva_columna]]
                productos.append(producto)
                print("Producto agregado exitosamente.")
                print(productos)
                return productos
        else:
            print("La ubicación ingresada no es válida. Por favor, ingrese una nueva fila y/o columna válida.")

#2
def baja_de_productos(productos: list) -> list:
    '''
    Recibe: La lista de productos.
    Valida: -
    Retorna: La lista actualizada de productos después de eliminar el producto especificado.
    '''
    nombre = input("Ingrese el nombre del producto que desea dar de baja: ")

    # Buscamos el producto por su nombre y lo eliminamos de la lista
    for producto in productos:
        if producto[0] == nombre:
            productos.remove(producto)
            print("Producto dado de baja correctamente.")
            print(productos)
            break
    else:
        print("El producto no fue encontrado.")

#3
def modificar_productos(productos: list) -> list:
    '''
    Recibe: La lista de productos.
    Valida: Verifica que la nueva posición esté dentro del rango permitido y que no esté ocupada por otro producto.
    Retorna: La lista actualizada de productos después de modificar un producto existente, o la misma lista si el producto no se encuentra.
    '''
    nombre = input("Ingrese el nombre del producto que desea modificar: ")

    for producto in productos:
        if producto[0] == nombre:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            while True:
                nueva_fila = int(input("Ingrese la nueva fila de la góndola (1, 2 o 3): "))
                nueva_columna = int(input("Ingrese la nueva columna de la góndola (1, 2, 3 o 4): "))

                # Verificamos que la fila y columna estén dentro del rango permitido
                validar_ubicacion = lambda fila, columna: 1 <= fila <= 3 and 1 <= columna <= 4
                if validar_ubicacion(nueva_fila, nueva_columna):
                    # Verificamos si la nueva posición está ocupada por otro producto
                    ubicacion_ocupada = False
                    for producto_a_modificar in productos:
                        if producto_a_modificar != producto and producto_a_modificar[2] == [nueva_fila, nueva_columna]:
                            ubicacion_ocupada = True
                            break

                    if ubicacion_ocupada:
                        print("La ubicación ingresada ya está ocupada por otro producto.")
                    else:
                        # Si llegamos aquí, la nueva posición no está ocupada por otro producto
                        # Si la nueva posición es la misma que la actual del producto, conservamos la posición
                        if [nueva_fila, nueva_columna] == producto[2]:
                            producto[1] = nueva_cantidad
                        else:
                            producto[1] = nueva_cantidad
                            producto[2] = [nueva_fila, nueva_columna]

                        print("Producto modificado correctamente.")
                        print(productos)
                        return productos
                else:
                    print("La ubicación ingresada no es válida. Por favor, ingrese una nueva fila y/o columna válida.")
    # Si se recorre toda la lista de productos y no se encuentra el producto
    print("El producto no fue encontrado en la lista.")
    return productos

#4
def listar_productos(productos: list) -> list:
    '''
    Recibe: La lista de productos.
    Valida: -
    Retorna: La misma lista de productos.
    '''
    if productos:
        print("Listado de productos:")
        for producto in productos:
            print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicación: {producto[2]}")
    else:
        print("No hay productos en la lista.")
    return productos

#5
def lista_productos_ordenados(productos: list) -> None:
    '''
    Recibe: La lista de productos.
    Valida: -
    Retorna: No retorna, solo imprime el listado de productos ordenado por nombre.
    '''
    if productos:
        # Algoritmo de ordenamiento de la burbuja
        for i in range(len(productos) - 1):
            for j in range(i+1, len(productos)):
                if(productos[i] > productos[j]):
                    aux = productos[i]
                    productos[i] = productos[j]
                    productos[j] = aux
        print("Listado de productos ordenado por nombre:")
        for producto in productos:
            print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicación: {producto[2]}")
    else:
        print("No hay productos en la lista.")

