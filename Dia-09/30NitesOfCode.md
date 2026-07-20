## Día 9 de #30NitesofCode 🚀

```python
# Atrapar errores para que el programa no se rompa

try:
    numero = int(input("Ingresa un número: "))
    print(f"El doble es {numero * 2}")
except ValueError:
    print("❌ Eso no es un número válido.")
finally:
    print("Bloque siempre se ejecuta.")
```

**Conceptos cubiertos:**
- `try` — bloque donde puede ocurrir un error.
- `except` — maneja el error específico (o genérico con `Exception`).
- `else` — se ejecuta si NO hubo error.
- `finally` — se ejecuta SIEMPRE (haya o no error).
- `raise` — lanza una excepción intencionalmente.

### Instrucciones

Crea un archivo `dia9.py` y escribe un programa que:

- [​✅] Defina una función `leer_entero(mensaje)` que pida un número y lo retorne como int.
- [​✅] Si el usuario ingresa algo que no es número, capturar `ValueError` y mostrar mensaje.
- [​✅] La función debe seguir pidiendo hasta que se ingrese un número válido.
- [​✅] Prueba la función pidiendo edad, cantidad de productos, y código postal.

> Los errores no son fracasos, son oportunidades de aprender. ¡A manejarlos! 🛡️
