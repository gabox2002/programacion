'''
Ejercicio 7: 
Crear una función lambda que devuelva el texto “femenino” si recibe el
valor “f” y sino “masculino”.
'''
obtener_genero = lambda valor: "femenino" if valor == "f" else "masculino" if valor == "m" else "género no definido"

genero = "f"
resultado = obtener_genero(genero)
print("El género es:", resultado)

