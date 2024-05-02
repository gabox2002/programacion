def reponer_mercaderia(estanteria, nombre, cantidad):
    for fila in estanteria:
        for cajon in fila:
            if nombre in cajon:
                index = cajon.index(nombre) + 1
                cajon[index] += cantidad
                print(f"Se han reponido {cantidad} unidades de '{nombre}'.")
                return
    print(f"Producto '{nombre}' no encontrado en la estantería.")

def vender_mercaderia(estanteria, nombre, cantidad):
    for fila in estanteria:
        for cajon in fila:
            if nombre in cajon:
                index = cajon.index(nombre) + 1
                stock = cajon[index]
                if stock >= cantidad:
                    cajon[index] -= cantidad
                    print(f"Se han vendido {cantidad} unidades de '{nombre}'.")
                    return
                else:
                    print(f"No hay suficiente stock de '{nombre}' para realizar la venta.")
                    return
    print(f"Producto '{nombre}' no encontrado en la estantería.")

def listar_inventario(estanteria):
    for fila in estanteria:
        for cajon in fila:
            print(f"Artículos en el cajón: {', '.join(map(str, cajon))}")
