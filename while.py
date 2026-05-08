#adivina el numero 

secreto = 7
 

while True:
    
    numero = float(input("adivina el numero secreto: ")) 
    
    if numero == secreto:
        print ("adivinaste!!")
        break
    elif numero < secreto:
        print("un poco mas arriba")
        continue
    elif numero > secreto:
        print("un poco mas abajo")
        continue
    else:
        print("error")
        break