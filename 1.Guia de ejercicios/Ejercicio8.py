'''
Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido
'''

lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
        #i  -->
            #j  -->


# Iteramos sobre cada índice en la lista
for i in range(len(lista)):
    # Iteramos sobre cada índice siguiente al actual en la lista
    for j in range(i + 1, len(lista)):
        # Comparamos el elemento en el índice i con el elemento en el índice j
        if lista[i] == lista[j]:
            # Si encontramos un número repetido, lo imprimimos
            print("El número repetido es:", lista[i])
            # Salimos del bucle interno, ya que hemos encontrado el número repetido
            break

        

#El bucle exterior (for i in range(len(lista))) itera sobre cada índice en la lista.
#El bucle interior (for j in range(i + 1, len(lista))) itera sobre cada índice siguiente al índice actual en la lista. Esto es para evitar comparaciones duplicadas y no comparar un elemento consigo mismo.
#En cada iteración del bucle interior, comparamos el elemento en el índice i con el elemento en el índice j.
#Si encontramos un número repetido, imprimimos ese número y luego salimos del bucle interno usando break, ya que no necesitamos seguir buscando una vez que hemos encontrado el número repetido.