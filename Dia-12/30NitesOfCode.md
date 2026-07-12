## Día 12 de #30NitesofCode 🚀

```python
# Comprensión: mismo resultado, menos código

# Tradicional
pares_trad = []
for i in range(10):
    if i % 2 == 0:
        pares_trad.append(i)

# Con comprensión
pares = [i for i in range(10) if i % 2 == 0]

print(pares)  # [0, 2, 4, 6, 8]

# Generador (bajo demanda)
gen = (i**2 for i in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]
```

**Conceptos cubiertos:**
- Comprensión de listas: `[expr for item in iterable if cond]`.
- Comprensión de diccionarios: `{k:v for k,v in iterable}`.
- Comprensión de sets: `{expr for item in iterable}`.
- Generadores con `yield` — producen valores bajo demanda (memoria eficiente).
- Generadores por comprensión: `(expr for item in iterable)`.

### Instrucciones

Crea un archivo `dia12.py` y escribe un programa que:

- [ ] Defina un generador `fibonacci(n)` con `yield` que genere los primeros n números.
- [ ] Pida al usuario cuántos números de Fibonacci quiere ver.
- [ ] Muestre la secuencia generada.
- [ ] Calcule la suma de esos números con `sum()`.

> Comprensiones: mucho poder en una sola línea. ¡A exprimir la sintaxis! 🍋
