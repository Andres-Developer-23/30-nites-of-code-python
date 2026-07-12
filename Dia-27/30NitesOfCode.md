## Día 27 de #30NitesofCode 🚀

```python
# SQLite: base de datos sin servidor
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", ("Ana",))
conn.commit()

cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())  # [(1, 'Ana')]
conn.close()
```

**Conceptos cubiertos:**
- `sqlite3.connect("archivo.db")` — conectar a BD.
- `cursor.execute("SQL")` — ejecuta sentencias SQL.
- `cursor.executemany("SQL", lista)` — múltiples valores.
- `conn.commit()` — guarda los cambios.
- `conn.close()` — cierra la conexión.
- `cursor.fetchall()` y `fetchone()`.
- SQL básico: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`.

### Instrucciones

Crea un archivo `dia27.py` y escribe un programa que:

- [ ] Cree una base de datos `inventario.db` con una tabla `productos`.
- [ ] La tabla debe tener: id, nombre, cantidad, precio.
- [ ] Inserta 5 productos de ejemplo.
- [ ] Muestre todos los productos con cantidad < 10 (bajo stock).
- [ ] Actualice la cantidad de un producto existente.
- [ ] Elimine un producto que ya no esté disponible.

> SQLite: base de datos sin complicaciones. ¡A almacenar! 🗄️
