#diccionario bucle for y .item()

dicc = {
    "pelota": 2 ,
    "juguete": 4,
    "pintura": 8}

for clave, valor in dicc.items():
    print(clave.upper(),(valor *2)) 