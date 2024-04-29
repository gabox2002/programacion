'''
Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
compras on-line recientemente lanzado al mercado para ello necesita un programa
que le permita acceder a los datos relevados.

Realizar una función con el siguiente Menú de Opciones:

1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal
sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
años.

Ejercicio 8: Crear una función para cada opción de menú.

Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación
de las listas.
'''

from Ejercicio9_Biblioteca import *

# Definición del menú de opciones
def menu():
    """
    Muestra el menú de opciones.
    """
    print("\nMenú de Opciones:")
    print("1. Importar listas")
    print("2. Listar los datos de los usuarios de México")
    print("3. Listar los nombre, mail y teléfono de los usuarios de Brasil")
    print("4. Listar los datos del/los usuario/s más joven/es")
    print("5. Obtener un promedio de edad de los usuarios")
    print("6. De los usuarios de Brasil, listar los datos del usuario de mayor edad")
    print("7. Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
    print("8. Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
    print("9. Salir")

# Función principal
def main():
    # Variables para almacenar las listas de datos
    nombres = []
    telefonos = []
    mails = []
    address = []
    postalZip = []
    region = []
    country = []
    edades = []

    # Bucle para mostrar el menú y ejecutar las opciones
    while True:
        menu()  # Mostrar el menú
        opcion = input("\nIngrese el número de la opción deseada: ")

        # Opción 1: Importar listas
        if opcion == "1":
            nombres, telefonos, mails, address, postalZip, region, country, edades = importar_listas()
            print("Listas importadas exitosamente.")

        # Opción 2: Listar los datos de los usuarios de México
        elif opcion == "2":
            if nombres:
                listar_usuarios_mexico(nombres, country)
            else:
                print("Primero debe importar las listas.")

        # Opción 3: Listar los nombre, mail y teléfono de los usuarios de Brasil
        elif opcion == "3":
            if nombres:
                listar_usuarios_brasil(nombres, mails, telefonos, country, postalZip)
            else:
                print("Primero debe importar las listas.")

        # Opción 4: Listar los datos del/los usuario/s más joven/es
        elif opcion == "4":
            if nombres:
                usuarios_jovenes = listar_usuario_mas_joven(nombres, country, edades)
                print("Usuario/s más joven/es:")
                for usuario in usuarios_jovenes:
                    print(f"{usuario[0]} de {usuario[1]} con {usuario[2]} años")
            else:
                print("Primero debe importar las listas.")

        # Opción 5: Obtener un promedio de edad de los usuarios
        elif opcion == "5":
            if edades:
                promedio = obtener_promedio_edad(edades)
                print(f"El promedio de edad de los usuarios es: {promedio}")
            else:
                print("Primero debe importar las listas.")

       # Opción 6: De los usuarios de Brasil, listar los datos del usuario de mayor edad
        elif opcion == "6":
            if nombres:
                persona_mayor_brasil = usuario_mayor_edad_brasil(nombres, edades, country)
                if persona_mayor_brasil:
                    print("Usuario/s de Brasil de mayor edad: ")
                    for usuario in persona_mayor_brasil:
                        print(f"{usuario[0]} con {usuario[1]} años")
                else:
                    print("No se encontraron personas de Brasil.")
            else:
                print("Primero debe importar las listas.")

        # Opción 7: Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
        elif opcion == "7":
            if nombres:
                usuarios_mexico_brasil_postal(nombres, postalZip, country)
            else:
                print("Primero debe importar las listas.")

        # Opción 8: Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años
        elif opcion == "8":
            if nombres:
                usuarios_italianos_mayores_40(nombres, edades, country, mails, telefonos)
            else:
                print("Primero debe importar las listas.")

        # Opción 9: Salir del programa
        elif opcion == "9":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
