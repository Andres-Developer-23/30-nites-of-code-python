## Día 29 de #30NitesofCode 🚀

```python
# Proyecto: API REST con Flask + SQLite
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("notas.db") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, contenido TEXT)")

init_db()

@app.route("/notas", methods=["GET"])
def listar():
    with sqlite3.connect("notas.db") as conn:
        notas = conn.execute("SELECT * FROM notas").fetchall()
    return jsonify([{"id": n[0], "titulo": n[1], "contenido": n[2]} for n in notas])

if __name__ == "__main__":
    app.run(debug=True)
```

**Conceptos cubiertos:**
- Integración de Flask + SQLite en una API completa.
- CRUD completo: Create (POST), Read (GET), Update (PUT), Delete (DELETE).
- `with sqlite3.connect()` como context manager.
- Buenas prácticas: separar lógica, usar JSON, códigos HTTP.

### Instrucciones

Crea un archivo `dia29.py` y escribe un programa que:

- [ ] Tome el código de ejemplo y complételo con los endpoints que faltan.
- [ ] Endpoint POST `/notas` — crea una nueva nota desde JSON.
- [ ] Endpoint PUT `/notas/<id>` — actualiza una nota existente.
- [ ] Endpoint DELETE `/notas/<id>` — elimina una nota.
- [ ] Endpoint GET `/notas?q=texto` — busque notas por título.
- [ ] Pruebe todos los endpoints con curl o Postman.

> API REST: tu backend listo para el mundo. ¡A servir datos! 🚀
