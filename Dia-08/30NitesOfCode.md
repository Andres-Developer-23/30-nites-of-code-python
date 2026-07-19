## Día 8 de #30NitesofCode 🚀

```python
# Lambda: funciones exprés
doble = lambda x: x * 2
print(doble(5))  # 10

# *args: argumentos variables
def suma_todo(*args):
    return sum(args)

print(suma_todo(1, 2, 3, 4))  # 10

# **kwargs: argumentos con nombre
def mostrar_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

mostrar_info(nombre="Luis", edad=30)
```

**Conceptos cubiertos:**
- `lambda` — función anónima de una sola línea.
- `*args` — tupla de argumentos posicionales variables.
- `**kwargs` — diccionario de argumentos con nombre variables.
- `map(función, iterable)` — aplica función a cada elemento.
- `filter(función, iterable)` — filtra elementos según condición.

### Instrucciones

Crea un archivo `dia8.py` y escribe un programa que:

- [​✅] Tenga una lista de precios originales: `[100, 250, 75, 150, 300]`.
- [​✅] Use `map()` con una lambda para aplicar un 15% de descuento.
- [​✅] Use `filter()` para quedarse solo con los precios >= 150 después del descuento.
- [​✅] Muestre los precios originales, con descuento, y los filtrados.

> Lambda y args/kwargs: código elegante y flexible. ¡A compactar! ⚡
