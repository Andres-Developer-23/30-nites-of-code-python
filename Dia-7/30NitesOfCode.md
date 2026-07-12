## Día 7 de #30NitesofCode 🚀

```python
# Las funciones encapsulan lógica reutilizable

def saludar(nombre):
    return f"¡Hola, {nombre}! 👋"

def sumar(a, b):
    return a + b

print(saludar("Ana"))
print(sumar(5, 3))
```

**Conceptos cubiertos:**
- `def` — palabra clave para definir funciones.
- Parámetros y argumentos: valores que recibe la función.
- `return` — devuelve un valor (si no hay, devuelve `None`).
- Parámetros por defecto: `def funcion(param=valor)`.
- Scope: variables locales vs globales.

### Instrucciones

Crea un archivo `dia7.py` y escribe un programa que:

- [ ] Defina una función `area_circulo(radio)` que retorne π * radio².
- [ ] Defina una función `area_rectangulo(base, altura)`.
- [ ] Defina una función `area_triangulo(base, altura)`.
- [ ] Pida al usuario qué figura calcular y los datos necesarios.
- [ ] Muestre el área calculada.

> Las funciones son los bloques de construcción del código limpio. ¡A modularizar! 🧱
