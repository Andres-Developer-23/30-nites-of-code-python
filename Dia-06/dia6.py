inventario = {
    'laptop': {'nombre': 'Dell Inspiron', 'precio': 750},
    'mouse': {'nombre': 'Logitech G502', 'precio': 50},
    'monitor': {'nombre': 'Samsung 24"', 'precio': 150}
}

inventario['consola'] = {'nombre': 'PlayStation 5', 'precio': 500}
inventario['juego'] = {'nombre': 'Elder Ring', 'precio': 69}

total = 0
for key, value in inventario.items():
    nombre = value['nombre']
    precio = value['precio']
    print(f"{key}: {nombre}  Precio: ${precio}") 
    total += precio
inventario['juego'] = {'nombre': 'Elder Ring', 'precio': 80.5}

print(f"Total en inventario: {total}")