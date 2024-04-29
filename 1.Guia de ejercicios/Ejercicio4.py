# Ejercicio 4:
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.'

edad = int(input("Ingrese su edad: "))

estado_civil_valido = False
while estado_civil_valido == False:
    estado_civil = input("Ingrese su estado civil (Soltero/Casado/Divorciado/Viudo): ")
    
    # Verificar si el estado civil es válido
    if estado_civil in ["Soltero", "Casado", "Divorciado", "Viudo"]:
        estado_civil_valido = True
    else:
        print("Estado civil no válido. Por favor, ingrese un estado civil válido.")

# Verificar si la edad es menor a 18 y el estado civil no es "Soltero"
if edad < 18 and estado_civil != "Soltero":
    print("Es muy pequeño para NO ser soltero.")