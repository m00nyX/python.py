#calculadora de pares

while true:
    
    numero = int(input("ingrese un numero")) 

    if numero %2 == 0:
        print(f"el numero {numero} es par")
    elif numero ==0:
        print(f"tu numero es {numero} no puedes divdirlo por dos")
        