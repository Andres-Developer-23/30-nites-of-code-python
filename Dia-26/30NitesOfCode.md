## Día 26 de #30NitesofCode 🚀

```python
# Flask: tu primera API web
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando 🚀"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return jsonify({"mensaje": f"Hola, {nombre}"})

if __name__ == "__main__":
    app.run(debug=True)
```

**Conceptos cubiertos:**
- `Flask(__name__)` — crea la aplicación.
- `@app.route("/ruta")` — define una ruta/endpoint.
- Métodos HTTP: GET, POST, PUT, DELETE.
- `jsonify()` — convierte dict/list a JSON response.
- `request.json` — obtiene datos JSON del body.
- Parámetros de ruta: `/<tipo:nombre>`.
- Códigos de estado: 200, 201, 404, 500.

### Instrucciones

Crea un archivo `dia26.py` y escribe un programa que:

- [ ] Cree una API con Flask que gestione una lista de tareas.
- [ ] Endpoint GET `/tareas` — devuelve todas las tareas.
- [ ] Endpoint POST `/tareas` — recibe JSON y agrega una tarea.
- [ ] Endpoint DELETE `/tareas/<id>` — elimina una tarea por ID.
- [ ) Pruebe los endpoints con curl o desde otro script con requests.

> Flask: tu primer paso en el mundo web. ¡A servir! 🌐
