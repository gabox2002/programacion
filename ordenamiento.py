#metodo de burbujeo con Swap ordenamiento ascendente

lista=[6,3,8,5]

for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if(lista[i] > lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print("Lista ordenada en orden ascendente:", lista)

#metodo de burbujeo con Swap ordenamiento descendente
lista = [6, 3, 8, 5]

for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):  
        if lista[i] < lista[j]:  # Cambiar la condición de comparación
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print("Lista ordenada en orden descendente:", lista)

#Ejemplo de ordenamiento 
nombres =["Ana","Juan","Jose","Sol","Mario","Ramiro","Zoe","Ana"]

for i in range(len(nombres)-1):
    for j in range(i+1, len(nombres)):
        if(nombres[i] > nombres[j]):
            aux = nombres[i]
            nombres[i] = nombres[j]
            nombres[j] = aux
print("Lista ordenada en orden ascendente:", nombres)


#Ejemplo de ordenamiento con listas paralelas
nombres =["Ana","Juan","Jose","Sol","Mario","Ramiro","Zoe","Ana"]
edades = [ 34,    45,    24,    65,    31,     55,     38,   23]

print("Nombres ", nombres)
print("Edades ", edades)

for i in range(len(nombres)-1):
    for j in range(i+1, len(nombres)):
        if nombres[i] > nombres[j]:
            auxn = nombres[i]
            auxe = edades [i]

            nombres[i] = nombres[j]
            edades[i] = edades[j]

            nombres[j] = auxn
            edades[j] = auxe

        if nombres[i] == nombres[j]:
            if edades[i] > edades[j]:
                auxn = nombres[i]
                auxe = edades [i]

                nombres[i] = nombres[j]
                edades[i] = edades[j]

                nombres[j] = auxn
                edades[j] = auxe
#Otra forma
# for i in range(len(nombres)-1): # Iteración sobre la lista de nombres para comparar cada elemento con los demás
#     for j in range(i+1, len(nombres)): # Iteración sobre la lista desde el elemento siguiente al actual en i hasta el último elemento
#         if nombres[i] > nombres[j]:  # Comprobación si el nombre en la posición i es mayor que el nombre en la posición j
#             nombres[i], nombres[j] = nombres[j], nombres[i] #Si el nombre en la posición i es mayor que el nombre en la posición j, se intercambian los nombres y las edades correspondientes
#             edades[i], edades[j] = edades[j], edades[i]


print("Nombres", nombres)
print("Edades ", edades)

