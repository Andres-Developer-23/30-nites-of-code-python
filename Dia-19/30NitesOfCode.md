## Día 19 de #30NitesofCode 🚀

```python
# JSON: el formato de intercambio de datos
import json

persona = {
    "nombre": "Ana",
    "edad": 28,
    "hobbies": ["leer", "viajar"]
}

# Diccionario → JSON string
texto_json = json.dumps(persona, indent=2)
print(texto_json)

# JSON string → Diccionario
recuperado = json.loads(texto_json)
print(recuperado["nombre"])  # Ana
```

**Conceptos cubiertos:**
- `json.dumps()` — convierte dict/list a string JSON.
- `json.loads()` — convierte string JSON a dict/list.
- `json.dump()` — escribe JSON directamente a un archivo.
- `json.load()` — lee JSON desde un archivo.
- `requests.get()` — hace una petición HTTP GET.

### Instrucciones

Crea un archivo `dia19.py` y escribe un programa que:

- [ ] Consulte la API de clima: `https://wttr.in/Ciudad?format=j1` (ej: Madrid).
- [ ] Parsee la respuesta JSON y muestre: ciudad, temperatura actual, descripción.
- [ ] Maneje errores si la ciudad no existe o hay problemas de conexión.
- [ ] Guarde la respuesta JSON en un archivo `clima.json`.

> JSON es el idioma universal de las APIs. ¡A comunicarse! 🌐
