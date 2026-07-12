## Día 23 de #30NitesofCode 🚀

```python
# Pandas: DataFrames como hojas de cálculo
import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Sofía"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"]
}
df = pd.DataFrame(datos)
print(df)
print(df.describe())
print(df[df["Edad"] > 25])
```

**Conceptos cubiertos:**
- `pd.DataFrame()` — estructura tabular con filas y columnas.
- `pd.Series()` — una sola columna (como un array con índice).
- `df.head(n)`, `df.tail(n)` — primeras/últimas filas.
- `df.describe()` — estadísticas descriptivas.
- `df.info()` — información del DataFrame.
- Filtrado: `df[df['columna'] > valor]`.
- `df.groupby()` — agrupar datos para agregaciones.

### Instrucciones

Crea un archivo `dia23.py` y escribe un programa que:

- [ ] Cree o descargue un CSV con datos de ventas (producto, cantidad, precio, fecha).
- [ ] Lea el CSV con `pd.read_csv()`.
- [ ] Muestre las primeras 5 filas y estadísticas descriptivas.
- [ ] Filtre las ventas con cantidad > 10.
- [ ] Calcule el total de ingresos por producto con `groupby()`.

> Pandas: el Excel de los programadores. ¡A tabular! 📊
