estudiantes = ["Carlos", "Ana", "Luis"]

diccionario = {}

for nombre in estudiantes:
    diccionario[nombre.upper()] = len(nombre)

print(diccionario)