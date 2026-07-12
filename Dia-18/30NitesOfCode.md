## Día 18 de #30NitesofCode 🚀

```python
# Las expresiones regulares buscan patrones en texto

import re

texto = "Mi email es hola@ejemplo.com y mi web es https://python.org"

email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
resultado = re.search(email, texto)
if resultado:
    print("Email:", resultado.group())
```

**Conceptos cubiertos:**
- `re.search()` — busca el patrón en todo el string.
- `re.findall()` — encuentra todas las coincidencias.
- `re.match()` — busca al inicio del string.
- `re.sub()` — reemplaza coincidencias.
- `re.split()` — divide el string por el patrón.
- Metacaracteres: `.`, `^`, `$`, `*`, `+`, `?`, `{}`, `[]`, `()`, `|`, `\`.

### Instrucciones

Crea un archivo `dia18.py` y escribe un programa que:

- [ ] Pida al usuario su email y valide el formato con `re.match()`.
- [ ] Pida un número de teléfono español (formato: +34 612 345 678) y valídelo.
- [ ] Extraiga todas las palabras de un texto que empiecen con mayúscula.
- [ ] Reemplace todos los números de un texto por "[NUM]" usando `re.sub()`.

> Las regex son el bisturí del texto. ¡A dominar los patrones! 🔪
