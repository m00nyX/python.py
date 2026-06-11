#prueba   while + acumulador

x = 0

while True:

    numero = int(input("ingrese un numero "))

    if numero >=0:
        x = x + numero
        print (x)
    
    else:
        print("la suma total es:")
        print(x)
        break 