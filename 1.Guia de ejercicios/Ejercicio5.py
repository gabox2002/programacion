'''
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
  -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
 descuento del 10% Mar del Plata tiene un descuento del 20%
  -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
 un aumento del 10% Mar del Plata tiene un aumento del 20%
   -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos
'''
while True:
    estacion = input("Ingrese la estación del año (Invierno/Verano/Otoño/Primavera): ").capitalize()
    if estacion in ["Invierno", "Verano", "Otoño", "Primavera"]:
        break
    else:
        print("Estación del año no válida. Ingrese una estación del año (Invierno/Verano/Otoño/Primavera)")

while True:
    localidad = input("Ingrese la localidad para vacacionar (Bariloche/Cataratas/Mar del Plata/Córdoba): ").capitalize()
    if localidad in ["Bariloche", "Cataratas", "Mar del Plata", "Córdoba"]:
        break
    else:
        print("Localidad no válida. Ingrese una localidad para vacacionar (Bariloche/Cataratas/Mar del Plata/Córdoba)")

precio_base = 15000

factor_estacion = 1.00
factor_localidad = 1.00

if estacion == "Invierno":
    if localidad == "Bariloche":
        factor_localidad = 1.20
    elif localidad == "Cataratas" or localidad == "Córdoba":
        factor_localidad = 0.90
    elif localidad == "Mar del Plata":
        factor_localidad = 0.80
elif estacion == "Verano":
    if localidad == "Bariloche":
        factor_localidad = 0.80
    elif localidad == "Cataratas" or localidad == "Córdoba":
        factor_localidad = 1.10
    elif localidad == "Mar del Plata":
        factor_localidad = 1.20
elif estacion == "Otoño" or estacion == "Primavera":
    if localidad == "Bariloche" or localidad == "Cataratas" or localidad == "Mar del Plata":
        factor_localidad = 1.10

precio_final = precio_base * factor_estacion * factor_localidad

print(f"El precio final del viaje a {localidad} en {estacion} es: ${precio_final:.2f}")

