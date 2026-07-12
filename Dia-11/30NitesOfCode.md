## Día 11 de #30NitesofCode 🚀

```python
# Escribir y leer archivos de texto

with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")

with open("ejemplo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)
```

**Conceptos cubiertos:**
- `open(archivo, modo)` — abre un archivo (modos: `r`, `w`, `a`, `r+`).
- `with open() as archivo` — gestor de contexto (cierra automáticamente).
- `write()` — escribe texto en el archivo.
- `read()` — lee todo el contenido.
- `readlines()` — lee todas las líneas como lista.
- Modos adicionales: `b` (binario), `encoding="utf-8"` para caracteres especiales.

### Instrucciones

Crea un archivo `dia11.py` y escribe un programa que:

- [ ] Pida al usuario que escriba una entrada de diario.
- [ ] Guarde cada entrada en `diario.txt` con la fecha y hora actual al inicio.
- [ ] Cada nueva entrada se agrega al final del archivo (modo `a`).
- [ ] Muestre todas las entradas guardadas al iniciar el programa.

> Los archivos son la memoria persistente de tus programas. ¡A guardar datos! 💾
