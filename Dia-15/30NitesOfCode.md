## Día 15 de #30NitesofCode 🚀

```python
# Un decorador envuelve una función para extenderla

def mayusculas(func):
    def wrapper():
        resultado = func()
        return resultado.upper()
    return wrapper

@mayusculas
def saludar():
    return "hola, mundo"

print(saludar())  # HOLA, MUNDO
```

**Conceptos cubiertos:**
- Decorador — función que envuelve a otra para extender su comportamiento.
- Sintaxis: `@decorador` sobre la función a decorar.
- `wrapper(*args, **kwargs)` — la función interna que envuelve.
- `functools.wraps` — preserva los metadatos de la función original.
- Decoradores útiles: `@staticmethod`, `@classmethod`, `@property`.

### Instrucciones

Crea un archivo `dia15.py` y escribe un programa que:

- [ ] Cree un decorador `@log` que imprima "Llamando a [nombre]" antes de ejecutar.
- [ ] Cree un decorador `@tiempo` que mida y muestre cuánto tarda la función.
- [ ] Aplique `@tiempo` a una función que calcule la suma de 1 a 100,000.
- [ ] Aplique `@log` y `@tiempo` a una función existente.

> Los decoradores envuelven tu código con superpoderes. ¡A decorar! 🎀
