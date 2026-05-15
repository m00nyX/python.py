#diccionario
bodega = [
    {"nombre": "Mouse", "precio": 15000, "stock": 10},
    {"nombre": "Teclado", "precio": 25000, "stock": 0},
    {"nombre": "Monitor", "precio": 120000, "stock": 5},
    {"nombre": "Cable HDMI", "precio": 8000, "stock": 0}
]

print("--- INFORME DE BODEGA ---")

total_inversion = 0

# El FOR va viendo un alemento a la vez de la bodega y lo guarda en la variable 'item'
for item in bodega:
    
    # 1. IF sirve para revisar si no hay productos en la bodega
    if item["stock"] == 0:
        print(f"ALERTA: El producto {item['nombre']} está agotado. ¡Pedir reposición!")
    else:
        # 2. Operación: Calculamos valor en nueva variabe por productos y sumamos al total
        valor_en_stock = item["precio"] * item["stock"]
        total_inversion += valor_en_stock
        print(f"{item['nombre']}: Hay {item['stock']} unidades disponibles.")

print("-" * 30)
print(f"Capital total invertido en stock: ${total_inversion}")
