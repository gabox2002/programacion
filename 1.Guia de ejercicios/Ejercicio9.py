'''
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
'''
#LISTAS PARALELAS
edades = [25,36,18,23,45]
nombres = ["Juan","Ana","Sol","Mario","Sonia"]

# Suponemos que la primera persona en la lista es la más joven inicialmente
indice_persona_menor = 0

# Iteramos sobre las edades para encontrar la posición de la persona más joven
for i in range(len(edades)):
    # Comparamos la edad actual con la edad de la persona más joven encontrada hasta ahora
    if edades[i] < edades[indice_persona_menor]:
        # Si encontramos una edad menor, actualizamos el índice de la persona más joven
        indice_persona_menor = i

# Después de iterar, tenemos el índice de la persona más joven
# Usamos este índice para obtener su nombre
nombre_persona_menor = nombres[indice_persona_menor]
edad_persona_menor = edades[indice_persona_menor]


print("La persona más joven es:", nombre_persona_menor)
print("Y su edad es: ", edad_persona_menor)




'''
En este código:

Utilizamos un bucle for para iterar sobre las edades y encontrar la posición de la persona más joven.
Comparamos cada edad con la edad de la persona más joven encontrada hasta ese momento, y si encontramos una edad menor, actualizamos el índice de la persona más joven.
Después de la iteración, usamos el índice de la persona más joven para obtener su nombre de la lista de nombres.
Finalmente, imprimimos el nombre de la persona más joven.
'''