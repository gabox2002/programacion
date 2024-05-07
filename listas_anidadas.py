# #Listas Anidadas
# nombres = ["Ana", "Juan", "Sol", "Luis", "Roberto"]
# edades = [23,       45,     34,     23,      46    ]
# telefono = [[123.345],[456,567],[678,987], [321]]

# #Ej
# contactos = [["Ana", 23],["Juan", 45],["Sol", 65]]

# print(contactos) #(['Ana', 23], ['Juan', 45], ['Sol', 65])
# print(contactos[1])  #[['Juan', 45]]

# print(contactos[1][1])  #45

# #Modificar los elementos
# print(contactos[2][1]) # 65
# contactos[2][1] = 66
# print(contactos[2][1]) # 06

# #Agregar elemento  APPEND
# contactos.append(["Luis"])  #[['Ana', 23], ['Juan', 45], ['Sol', 66], ['Luis']]
# print(contactos)

# #Agregar edad a Luis
# contactos[3].append(22)  #[['Ana', 23], ['Juan', 45], ['Sol', 65], ['Luis', 22]]
# print(contactos)

# #Recorrer elementos
# for e_contacto in contactos:
#     print(e_contacto[0], e_contacto[1]) #Ana 23
#                                         #Juan 45
#                                         #Sol 65
#                                         #Luis 22
# #Eliminar elementos POP
# print(contactos)                                    #[['Ana', 23], ['Juan', 45], ['Sol', 65], ['Luis', 22]]

# contactos.pop() #elimina el ultimo
# print(contactos)                                    #[['Ana', 23], ['Juan', 45], ['Sol', 65]]

# contactos.pop(2) #elimina a Sol
# print(contactos)                                    #[['Ana', 23], ['Juan', 45]]

# contactos[3].pop() #elimina la edad 22 de Luis      
# print(contactos)                                    #[['Ana', 23], ['Juan', 45], ['Sol', 65], ['Luis']]

#Ej
# def mostrar():
#     for contacto in lista_contactos:
#         print(contacto)
#     print("\n")

# nombres = ["Ana", "Juan", "Sol", "Luis", "Roberto"]
# edades = [23,       45,     34,     23,      46    ]
# telefono = [[123.345],[456,567],[678,987], [321]]

# lista_contactos = [ ["Ana", 23, [123,345]], #nombre, edad, telefonos
#                     ["Juan", 45, [456,567]], 
#                     ["Sol", 34, [678,987]], 
#                     ["Luis", 23, [356]]
#                     ]
# mostrar()
# #Borrar a Luis
# lista_contactos.pop(3)
# print("Borrar a Luis")
# mostrar()

# #Borrar el 2do telefono de Sol
# lista_contactos[2][2].pop(1)
# print("Borrar el segundo telefono de Sol")
# mostrar()

# #Agregamos un nuevo contacto
# lista_contactos.append(["Roberto",46,[321]])
# print("Agregamos un nuevo contacto")
# mostrar()

# #Modificar / Actualizar un año Luis que fue su cumple
# lista_contactos[3][1] += 1   #Acumulador -> lista_contactos[3][1] = lista_contactos[3][1] + 1
# print("Agregamos un año a Luis")
# mostrar()

# #Ordenamos por nombre
# for i in range(len(lista_contactos)-1):
#     for j in range(i+1, len(lista_contactos)):
#         if(lista_contactos[i][0] > lista_contactos[j][0]):  #[0] porque quiero que ordene por nombre
#             lista_aux = lista_contactos[i]
#             lista_contactos[i] = lista_contactos[j]
#             lista_contactos[j] = lista_aux
# print("Lista ordenadas por nombre")
# mostrar()

# #Ordenamos por edad
# for i in range(len(lista_contactos)-1):
#     for j in range(i+1, len(lista_contactos)):
#         if(lista_contactos[i][1] > lista_contactos[j][1]):  #[1] porque quiero que ordene por edad
#             lista_aux = lista_contactos[i]
#             lista_contactos[i] = lista_contactos[j]
#             lista_contactos[j] = lista_aux
# print("Lista ordenadas por edad")
# mostrar()


# #Ej almacen
# def mostrar():
#     for producto in productos:
#         print(producto)
#     print("\n")

# productos = [["botellas", 3, [1,2]],
#            ["frascos", 8, [1,4]],
#            ["fideos", 4, [2,3]],
#            ["leche", 6, [3,4]]
#            ]

# mostrar()

# #Nuevo producto aceite, 10 en [3,2]
# productos.append(["aceite", 10, [3,2]])
# print("Agrego el aceite")
# mostrar()

# #Vender 2 aceites
# productos_a_vender = "aceite"
# cuantos = 2
# for producto in productos:
#     if producto[0] == productos_a_vender:
#         producto[1] -= cuantos
#         break

# mostrar()

# #Mover los fideos a [2,4]
# productos[2][2][1] = 4
# mostrar()


# #Ej ferreteria
# def mostrar():
#     for cajon in estanteria:
#         print(cajon)
#         for fila in cajon:
#             print(fila[0], fila[1])
#     print("\n")

# estanteria = [
#             [["to12",65],["to16",86],["to20",65],["to25",45]],
#             [["to30",68],["to35",73],["to40",85],["to45",89]],
#             [["ta4",58],["ta5",48],["ta6",64],["ta7",96]],
#             [["ta8",36],["ta10",72],["ta12",78],["ta14",71]]
#             ]

# mostrar()

# producto = input("Ingrese el poducto a reponer: ")
# cantidad = int(input("Ingrese cantidad: "))

# for cajon in estanteria:
#     for fila in cajon:
#         if fila[0] == producto:
#             fila[1] += cantidad

# mostrar()