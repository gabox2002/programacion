'''
Ejercicio 9: Desarrollar las funciones en una biblioteca.

Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación
de las listas.
'''

from listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades

# Función para importar listas
def importar_listas():
    """
    Recibe: No recibe ningún argumento.
    Valida: No realiza validaciones en este caso.
    Retorna: Listas de usuarios importadas desde el archivo listas_personas.py.
    """
    # Se importan las listas de usuarios desde el archivo listas_personas.py
    return nombres, telefonos, mails, address, postalZip, region, country, edades

# Función para listar los datos de los usuarios de México
def listar_usuarios_mexico(nombres, country):
    """
    Recibe: nombres (list): Lista de nombres de usuarios.
            region (list): Lista de regiones de usuarios.
    Valida: No realiza validaciones en este caso.
    Retorna: Lista de nombres de usuarios que pertenecen a México.
    """
    print("Usuarios de México:")
    for i in range(len(country)):
        if country[i] == "Mexico":
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}, Teléfono: {telefonos[i]}, Zip: {postalZip[i]}")

# Función para listar los nombre, mail y teléfono de los usuarios de Brasil
def listar_usuarios_brasil(nombres, mails, telefonos, country, postalZip):
    """
    Recibe: nombres (list): Lista de nombres de usuarios.
            mails (list): Lista de correos electrónicos de usuarios.
            telefonos (list): Lista de números de teléfono de usuarios.
            country (list): Lista de países de usuarios.
    Valida: No realiza validaciones en este caso.
    Retorna: Lista de nombres, correos electrónicos y números de teléfono de usuarios que pertenecen a Brasil.
    """
    print("Usuarios de Brasil:")
    for i in range(len(country)):
        if country[i] == "Brazil":
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}, Teléfono: {telefonos[i]}, Zip: {postalZip[i]}")

# Función para listar los datos del/los usuario/s más joven/es
def listar_usuario_mas_joven(nombres, country, edades):
    """
    Recibe: nombres (list): Lista de nombres de usuarios.
            edades (list): Lista de edades de usuarios.
    Valida: No realiza validaciones en este caso.
    Retorna: Lista de nombres de usuarios más jóvenes.
    """
    min_edad = edades[0]
    usuarios_mas_jovenes = [] 

    # Iterar sobre la lista de edades
    for i in range(len(edades)):
        # Verificar si la edad actual es menor que la edad mínima
        if edades[i] <= min_edad:
            # Actualizar la edad mínima
            min_edad = edades[i]
            usuarios_mas_jovenes.append((nombres[i], country[i], edades[i])) # Limpiar la lista de personas más jóvenes y agregar la nueva persona más joven

        
    return usuarios_mas_jovenes

# Función para obtener un promedio de edad de los usuarios
def obtener_promedio_edad(edades):
    """
    Recibe: edades (list): Lista de edades de usuarios.
    Valida: No realiza validaciones en este caso.
    Retorna: Promedio de edades de los usuarios.
    """
    return sum(edades) / len(edades)

# Función para listar los datos del usuario de Brasil de mayor edad
def usuario_mayor_edad_brasil(nombres, edades, country):
    """
    Recibe:
        nombres (list): Lista de nombres de usuarios.
        edades (list): Lista de edades de usuarios.
        country (list): Lista de países de usuarios.
    Valida:
        No realiza validaciones en este caso.
    Retorna:
        Datos del usuario de Brasil de mayor edad.
    """
    mayor_edad = edades[0]
    persona_mayor = []

    for i in range(len(edades)):
        # Verificar si la persona es de Brasil
        if country[i] == "Brazil":
            # Verificar si la edad actual es mayor que la edad máxima
            if edades[i] >= mayor_edad:
                # Actualizar la edad máxima
                mayor_edad = edades[i]
                persona_mayor.append((nombres[i], edades[i]))

    return persona_mayor


# Función para listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
def usuarios_mexico_brasil_postal(nombres, postalZip, country):
    """
    Recibe:
        nombres (list): Lista de nombres de usuarios.
        region (list): Lista de regiones de usuarios.
        postalZip (list): Lista de códigos postales de usuarios.
    Valida:
        No realiza validaciones en este caso.
    Retorna:
        Lista de datos de usuarios de México y Brasil cuyos códigos postales sean mayores a 8000.
    """
    # Bandera para verificar si se encontraron usuarios que cumplan con los criterios
    usuarios_encontrados = False
    
    # Iterar sobre la lista de nombres
    for i in range(len(nombres)):
        # Verificar si el país es México o Brasil y si el código postal es mayor a 8000
        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:
            print(f"Nombre: {nombres[i]}, País: {country[i]}, Código Postal: {postalZip[i]}")
            usuarios_encontrados = True
    
    # Verificar si no se encontraron usuarios que cumplan con los criterios
    if not usuarios_encontrados:
        print("No se encontraron usuarios de México y Brasil con código postal mayor a 8000.")
# Función para listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años
def usuarios_italianos_mayores_40(nombres, edades, country, mails, telefonos):
    """
    Recibe: nombres (list): Lista de nombres de usuarios.
            edades (list): Lista de edades de usuarios.
            country (list): Lista de países de usuarios.
            mails (list): Lista de correos electrónicos de usuarios.
            telefonos (list): Lista de números de teléfono de usuarios.
    Valida: No realiza validaciones en este caso.
    Retorna: Lista de nombres, correos electrónicos y números de teléfono de usuarios italianos mayores a 40 años.
    """
    print("Usuarios italianos mayores de 40 años:")
    for i in range(len(country)):
        if country[i] == "Italy" and edades[i] > 40:
            print(f"Nombre: {nombres[i]}, Email: {mails[i]}, Teléfono: {telefonos[i]}, Edad:{edades[i]}")
