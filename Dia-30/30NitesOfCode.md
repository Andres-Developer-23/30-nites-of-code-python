## Día 30 de #30NitesofCode 🚀

```python
# Proyecto Final: Pipeline completo de datos
# scrape → limpiar → analizar → visualizar → exportar → servir

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import json
import sqlite3

def scrapear(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup

def analizar(df):
    return df.describe()

def exportar(df):
    df.to_csv("datos.csv", index=False)
    with sqlite3.connect("datos.db") as conn:
        df.to_sql("datos", conn, if_exists="replace", index=False)

print("🎉 #30NitesofCode completado!")
print("30 días, 30 lecciones, un nuevo programador. ¡Sigue codeando!")
```

**Conceptos cubiertos:**
- Pipeline completo de datos.
- Integración de todas las librerías aprendidas.
- Exportación a múltiples formatos.
- Código modular y organizado.

### Instrucciones

Crea un archivo `dia30.py` y escribe un programa que:

- [ ] Implemente cada función del pipeline con datos reales.
- [ ] `scrapear()`: extraiga datos de una web pública real.
- [ ] Convierta los datos a DataFrame y limpie valores nulos.
- [ ] `analizar()`: calcule media, mediana, percentiles, y outliers.
- [ ] Genere 3 visualizaciones diferentes (líneas, barras, pastel).
- [ ) `exportar()`: guarde a CSV, JSON y SQLite.
- [ ] Suba su proyecto a GitHub y comparta con #30NitesofCode.

> 🏆 ¡LO LOGRASTE! 30 días, 30 noches, un nuevo capítulo en tu vida como programador.
>
> *"El viaje de mil millas comienza con un solo paso." — Lao Tsé*
>
> **#Python #30NitesofCode #CodeEveryday**
