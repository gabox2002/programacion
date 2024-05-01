'''
Ejercicio 7: 
Crear una función lambda que devuelva el texto “femenino” si recibe el
valor “f” y sino “masculino”.
'''
obtener_genero = lambda valor: "femenino" if valor == "f" else "masculino" if valor == "m" else "no definido"

print(f"El género es: {obtener_genero("k")}")

