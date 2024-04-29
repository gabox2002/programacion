#Ejercicio 2
#Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
#adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    resultado = "mayor de edad"
elif 13 <= edad <= 17:
    resultado = "adolescente"
else:
    resultado = "niño"

print(f"La persona es {resultado}")