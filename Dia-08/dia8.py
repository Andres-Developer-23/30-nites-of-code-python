precios = [100, 250, 75, 150, 300]

descuento = list(map(lambda x: x * 0.85, precios))
filtrados = list(map(lambda x: x >= 150, precios))

print(f"Precios originales: {precios}")
print(f"Con 15% de descuento: {descuento}")
print(f"Filtrados (>= 150):   {filtrados}")