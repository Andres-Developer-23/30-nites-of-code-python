## Día 20 de #30NitesofCode 🚀

```python
# map, filter y reduce: procesar colecciones sin bucles explícitos
from functools import reduce

nums = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x**2, nums))
pares = list(filter(lambda x: x % 2 == 0, nums))
suma = reduce(lambda a, b: a + b, nums)

print(cuadrados)  # [1, 4, 9, 16, 25]
print(pares)      # [2, 4]
print(suma)       # 15
```

**Conceptos cubiertos:**
- `map(función, iterable)` — aplica función a cada elemento.
- `filter(función, iterable)` — filtra elementos según condición True.
- `reduce(función, iterable)` — acumula elementos en un solo valor.
- `functools` — módulo con herramientas funcionales.
- `partial()` — fija argumentos de una función.

### Instrucciones

Crea un archivo `dia20.py` y escribe un programa que:

- [ ] Tenga una lista de transacciones: `[("compra", 100), ("venta", 250), ("compra", 50), ("venta", 180)]`.
- [ ] Use `filter()` para quedarse solo con las compras.
- [ ] Use `map()` para obtener solo los montos.
- [ ] Use `reduce()` para sumar el total de compras y el total de ventas.
- [ ] Muestre: total compras, total ventas, y balance final.

> Programación funcional: código declarativo y elegante. ¡A componer! 🧩
