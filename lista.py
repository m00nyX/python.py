# lista de promedio

numeros = []

for i in range (5):
    num = int(input("ingrese su numero: "))
    numeros.append(num)

numeros.sort(reverse=True)
print("lista ordenada:",numeros )

promedio = sum(numeros) / len(numeros) 
print("Promedio:", promedio)