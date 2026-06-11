paquetes = {}

cantidad = 0

while cantidad <= 0:
    cantidad = int(input("¿Cuántos paquetes se cargarán?: "))

for i in range(cantidad):
    print(f"Paquete {i+1}")

    codigo = input("Código del paquete: ").strip().upper()
    peso = float(input("Peso del paquete (kg): "))

    paquetes[codigo] = round(peso, 1)

print("---REPORTE DE CARGA---")
print("Paquetes registrados:")
print(paquetes)

print("Cantidad total de paquetes:", len(paquetes))