## Día 22 de #30NitesofCode 🚀

```python
# NumPy: arrays rápidos y operaciones vectorizadas
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)        # [2 4 6 8 10]
print(arr ** 2)       # [1 4 9 16 25]
print(arr > 3)        # [False False False  True  True]
print(arr.mean())     # 3.0
print(arr.sum())      # 15
```

**Conceptos cubiertos:**
- `np.array()` — crea un array de NumPy.
- `shape`, `ndim`, `dtype` — atributos del array.
- Arrays 2D (matrices) y multidimensionales.
- Operaciones vectorizadas (sin loops explícitos).
- `np.mean()`, `np.median()`, `np.std()`, `np.sum()`.
- `np.arange()`, `np.zeros()`, `np.ones()`, `np.linspace()`.

### Instrucciones

Crea un archivo `dia22.py` y escribe un programa que:

- [ ] Cree una matriz 5x5 con números aleatorios enteros del 1 al 100.
- [ ] Muestre la matriz, su forma, y su tipo de dato.
- [ ) Calcule y muestre: media, suma total, valor máximo y mínimo.
- [ ] Multiplique toda la matriz por 2.
- [ ] Extraiga la diagonal principal y la primera fila.

> NumPy: el motor numérico de Python. ¡A vectorizar! 🚀
