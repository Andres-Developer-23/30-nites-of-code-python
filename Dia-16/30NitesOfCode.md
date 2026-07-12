## Día 16 de #30NitesofCode 🚀

```python
# Iterador personalizado con __iter__ y __next__

class CuentaRegresiva:
    def __init__(self, inicio):
        self.inicio = inicio

    def __iter__(self):
        self.actual = self.inicio
        return self

    def __next__(self):
        if self.actual <= 0:
            raise StopIteration
        valor = self.actual
        self.actual -= 1
        return valor

for n in CuentaRegresiva(5):
    print(n, end=" ")  # 5 4 3 2 1
```

**Conceptos cubiertos:**
- Iterable — objeto que puede iterarse (listas, tuplas, strings, dicts).
- Iterador — objeto que produce valores uno a uno.
- `__iter__()` — devuelve el objeto iterador.
- `__next__()` — devuelve el siguiente valor o lanza `StopIteration`.
- `iter(iterable)` y `next(iterador)` — control manual.

### Instrucciones

Crea un archivo `dia16.py` y escribe un programa que:

- [ ] Cree un iterador `Pares` que genere números pares desde 0 hasta un límite N.
- [ ) Use un `for` para recorrer los primeros 10 pares.
- [ ] Use `iter()` y `next()` manualmente para obtener los primeros 5.
- [ ] Cree el mismo iterador pero usando un generador con `yield`.

> Iteradores: el protocolo que hace funcionar los bucles. ¡A iterar! 🔄
