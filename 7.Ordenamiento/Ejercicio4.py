'''
Ejercicio 4: 
Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line recientemente lanzado al mercado para ello necesita un programa que le permita acceder a los datos relevados.

Agregar los siguientes puntos al Menú de Opciones:
1-Importar listas
2-Listar los datos de los usuarios de México
3-Listar los nombre, mail y teléfono de los usuarios de Brasil
4-Listar los datos del/los usuario/s más joven/es
5-Obtener un promedio de edad de los usuarios
6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
9-Listar los datos de los usuarios de México ordenados por nombre
10-Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente)

11-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente

Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación
de las listas
'''

from Ejercicio4_Biblioteca import *

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
    print("9. Listar los datos de los usuarios de México ordenados por nombre")
    print("10. Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente")
    print("11. Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente")
    print("12. Salir")

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
                listar_usuarios_brasil(nombres, telefonos, country, postalZip)
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
                personas_postal_mayor_8000 = usuarios_mexico_brasil_postal(nombres, postalZip, country, edades)
                if personas_postal_mayor_8000:
                    print("Usuario/s de Mexico y Brasil con código postal mayor a 8000: ")
                    for usuario in personas_postal_mayor_8000:
                        print(f"Nombre: {usuario[0]}, País: {usuario[1]}, Código Postal: {usuario[2]}, Edad: {usuario[3]}")
                else: 
                    print("No se encontraron usuarios de México y Brasil con código postal mayor a 8000.")
            else:
                print("Primero debe importar las listas.")


        # Opción 8: Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años
        elif opcion == "8":
            if nombres:
                italianos_mayores_40 = usuarios_italianos_mayores_40(nombres, edades, country, mails, postalZip)
                if italianos_mayores_40:
                    print("Usuarios italianos mayores de 40 años:")
                    for usuario in italianos_mayores_40:
                        print(f"Nombre: {usuario[0]}, Edad:{usuario[1]}, Country:{usuario[2]}, Email: {usuario[3]}, CodigoPostal: {usuario[4]}")
                else: 
                    print("No se encontraron italianos mayores de 40")
            else:
                print("Primero debe importar las listas.")

        # Opción 9: Listar los datos de los usuarios de México ordenados por nombre
        elif opcion == "9":
            if nombres:
                usuarios_mexico_ordenados = listar_usuarios_mexico_ordenados_por_nombre(nombres, edades, country, postalZip)
                if usuarios_mexico_ordenados:
                    print("Datos de los usuarios de México ordenados por nombre:")
                    for usuario in usuarios_mexico_ordenados:
                        print(f"Nombre: {usuario[0]}, Edad: {usuario[1]}, País: {usuario[2]}, CodigoPostal: {usuario[3]}")
                else:
                    print("No se encontraron usuarios de México.")
            else:
                print("Primero debe importar las listas.")

        # Opción 10: Listar los datos del/los usuario/s más joven/es ordenados por nombre de manera ascendente
        elif opcion == "10":
            if nombres:
                # Obtener la lista de usuarios más jóvenes
                usuarios_mas_jovenes = listar_usuario_mas_joven(nombres, country, edades)
                
                # Ordenar los usuarios más jóvenes por nombre de manera ascendente
                usuarios_mas_jovenes_ordenados = ordenar_usuarios_mas_jovenes(usuarios_mas_jovenes)
                
                # Mostrar los usuarios más jóvenes ordenados
                if usuarios_mas_jovenes_ordenados:
                    print("Usuarios más jóvenes ordenados por nombre:")
                    for usuario in usuarios_mas_jovenes_ordenados:
                        print(f"Nombre: {usuario[0]}, Edad: {usuario[2]}, País: {usuario[1]}")
                else:
                    print("No se encontraron usuarios más jóvenes.")
            else:
                print("Primero debe importar las listas.")

        # Opción 11: Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente
        elif opcion == "11":
            if nombres:
                # Obtener la lista de usuarios mexico brazil postal
                usuarios_encontrados = usuarios_mexico_brasil_postal(nombres, postalZip, country, edades)

                # Ordenar los usuarios
                usuarios_ordenados = ordenar_usuarios_mas_jovenes(usuarios_encontrados)

                if usuarios_ordenados:
                    print("Usuarios de México y Brasil con código postal mayor a 8000, ordenados por nombre y edad de manera descendente:")
                    for usuario in usuarios_ordenados:
                        print(f"Nombre: {usuario[0]}, País: {usuario[1]}, Código Postal: {usuario[2]}, Edad: {usuario[3]}")
                else:
                    print("No se encontraron usuarios de México y Brasil con código postal mayor a 8000.")
            else:
                print("Primero debe importar las listas.")

        # Opción 12: Salir del programa
        elif opcion == "12":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
