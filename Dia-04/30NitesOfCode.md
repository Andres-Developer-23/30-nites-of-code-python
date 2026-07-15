## Día 4 de #30NitesofCode 🚀

```python
# Dos formas de repetir

# Con while
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
# Salida: 1 2 3 4 5

print()

# Con for
for i in range(1, 6):
    print(i, end=" ")
# Salida: 1 2 3 4 5
```

**Conceptos cubiertos:**
- `while` — repite mientras una condición sea verdadera.
- `for` — itera sobre una secuencia (range, lista, string).
- `range(inicio, fin, paso)` — genera secuencias numéricas.
- `break` — sale del bucle inmediatamente.
- `continue` — salta a la siguiente iteración.
- Bucles anidados — un bucle dentro de otro.

### Instrucciones

Crea un archivo `dia4.py` y escribe un programa que:

- [​✅] Pida al usuario la altura de un triángulo (ej: 5).
- [​✅] Dibuje un triángulo rectángulo de asteriscos con esa altura.
- [​✅] Ejemplo con altura 5:
  ```
  *
  **
  ***
  ****
  *****
  ```
- [​✅] Sume todos los números pares del 1 al 100 usando un bucle.

> Los bucles son la magia que hace mucho con poco código. ¡A repetir! 🔄
