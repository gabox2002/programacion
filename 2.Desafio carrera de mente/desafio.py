'''
Desafío Carrera de Mente

Set de datos

La información a ser analizada se encuentra en el archivo datos.py, por tratarse de
una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:
from datos import lista
Formato de los datos recibidos
lista=[
{'pregunta': '¿Cuándo finalizó la II Guerra Mundial?',
'a': '1945',
'b': '1954',
'c':'1937',
'correcta': 'a',
'tema': 'Historia'},
{'pregunta': '¿A qué editorial de comics pertenece Capitán América?',
'a': 'Marvel',
'b': 'DC',
'c': 'Ninguna',
'correcta': 'a',
'tema':'Cine'
}
]

Desafío:
A. Analizar detenidamente el set de datos.
B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción, el tema y la
respuesta correcta.
C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la
etiqueta “Reiniciar”
D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
correctas. Cada respuesta correcta suma 10 puntos.
E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar el tema y las
preguntas comenzando por la primera y las tres opciones, cada clic en este
botón pasa a la siguiente pregunta.
F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el score y dejar de mostrar las opciones.
G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si
agotó ambas opciones, deja de mostrar las opciones y no suma score
H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic pasa a la siguiente
pregunta. También debe reiniciar el Score.
'''