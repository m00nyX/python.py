#prueba   for-lista

lista = []

for i in range (5):
    
    numeros = int(input("ingrese un numero: "))
    lista.append(numeros)

    promedio = sum(lista) / len(lista)

print(f"lista:",(lista),
         "el promedio es:",(promedio),
         "el numero mayor es:",max(lista))