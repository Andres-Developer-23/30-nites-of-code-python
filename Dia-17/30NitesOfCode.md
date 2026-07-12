## Día 17 de #30NitesofCode 🚀

```python
# Un context manager gestiona recursos automáticamente

class Saludar:
    def __enter__(self):
        print("👋 Entrando...")
        return self

    def __exit__(self, *args):
        print("👋 Saliendo...")

with Saludar():
    print("  Dentro del bloque")
```

**Conceptos cubiertos:**
- `with` — sintaxis para usar context managers.
- `__enter__` — se ejecuta al entrar al bloque `with`.
- `__exit__` — se ejecuta al salir del bloque (haya o no error).
- `contextlib` — módulo con utilidades: `@contextmanager` con yield.
- Usos típicos: archivos, conexiones a BD, locks, temporizadores.

### Instrucciones

Crea un archivo `dia17.py` y escribe un programa que:

- [ ] Cree un context manager `Temporizador` que mida el tiempo dentro del bloque.
- [ ] `__enter__` registra el tiempo inicial, `__exit__` calcula y muestra la duración.
- [ ] Pruebe el Temporizador con un bloque que tenga un `time.sleep(1)`.
- [ ] Implemente el mismo Temporizador usando `@contextmanager` de `contextlib`.

> Context managers: recursos que se limpian solos. ¡A gestionar! 🧹
