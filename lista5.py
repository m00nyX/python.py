precios = [5000,2000,3500]

precios.insert(0,2000)
print ( precios)

precios.sort()

total = sum(precios)
cantidad = len(precios)

print(f"Lista ordenada: {precios}")
print(f"Tienes {cantidad} productos y el total es ${total}")