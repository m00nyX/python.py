#traductor de colores

inventario = {
    "red":"rojo",
    "blue":"azul",
    "yellow":"amarillo",
    "green":"verde",
    "purple":"morado"}

color = input("ingrese un color en ingles: ")

if color in inventario:
    print("traduccion:",(inventario [color]))
else:
    nuevo_color =input("el color no existe, porfavor agregar traduccion: ")
    inventario[color] = nuevo_color
    print("nuevo color agregado", nuevo_color)
