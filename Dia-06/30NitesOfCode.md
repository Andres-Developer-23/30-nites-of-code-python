## Día 6 de #30NitesofCode 🚀

```python
# Tres estructuras útiles

# Tupla (inmutable)
coordenadas = (40.4168, -3.7038)

# Set (sin duplicados)
lenguajes = {"Python", "Java", "Python", "JavaScript"}
print(lenguajes)  # {'Python', 'Java', 'JavaScript'}

# Diccionario (clave → valor)
capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}
print(capitales["España"])  # Madrid
```

**Conceptos cubiertos:**
- Tuplas `()` — inmutables, ideales para datos fijos.
- Sets `{}` — colecciones desordenadas sin duplicados.
- Diccionarios `{k:v}` — pares clave-valor.
- Métodos: `keys()`, `values()`, `items()`, `get()`.
- Iterar con `for clave, valor in dict.items()`.

### Instrucciones

Crea un archivo `dia6.py` y escribe un programa que:

- [​✅] Cree un diccionario `inventario` con 3 productos (clave = nombre, valor = precio).
- [​✅] Agregue 2 productos más.
- [​✅] Muestre todos los productos y precios.
- [​✅) Actualice el precio de un producto existente.
- [​✅] Calcule el precio total del inventario.

> Diccionarios: la navaja suiza de las estructuras de datos. ¡A explorar! 🔑
