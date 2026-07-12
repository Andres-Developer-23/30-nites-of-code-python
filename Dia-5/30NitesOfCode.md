## Día 5 de #30NitesofCode 🚀

```python
# Las listas son colecciones ordenadas
colores = ["rojo", "verde", "azul"]
colores.append("amarillo")
colores.insert(0, "naranja")
colores.remove("verde")

print(colores)               # ['naranja', 'rojo', 'azul', 'amarillo']
print(colores[0])            # naranja
print(colores[-1])           # amarillo
print(colores[1:3])          # ['rojo', 'azul']
print(len(colores))          # 4
```

**Conceptos cubiertos:**
- Listas — colecciones ordenadas y mutables con `[]`.
- Índices: empiezan en 0, índices negativos van del final.
- Slicing: `lista[inicio:fin:paso]` para obtener sublistas.
- Métodos: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`.
- `len()` — longitud de la lista.

### Instrucciones

Crea un archivo `dia5.py` y escribe un programa que:

- [ ] Cree una lista vacía `compras = []`.
- [ ] Muestre un menú: 1. Agregar item  2. Quitar item  3. Mostrar lista  4. Salir.
- [ ] Use `while` para mantener el menú corriendo hasta que el usuario elija salir.
- [ ] Muestre la lista ordenada alfabéticamente antes de salir.

> Las listas son el bolsillo mágico de Python. ¡A llenarlo de datos! 📦
