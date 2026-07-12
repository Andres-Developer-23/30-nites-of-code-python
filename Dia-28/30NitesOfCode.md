## Día 28 de #30NitesofCode 🚀

```python
# Proyecto integrador: scrape → analizar → visualizar
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Ejemplo de flujo (datos simulados para ilustrar)
datos = [
    {"producto": "Libro A", "precio": 12.99, "stock": 45},
    {"producto": "Libro B", "precio": 8.50, "stock": 120},
    {"producto": "Libro C", "precio": 15.00, "stock": 33},
]
df = pd.DataFrame(datos)
print(df.describe())
df.plot(kind="bar", x="producto", y="precio")
plt.show()
```

**Conceptos cubiertos:**
- Integración de BeautifulSoup + Pandas + Matplotlib en un proyecto.
- Flujo completo: extracción → limpieza → análisis → visualización.
- Exportar resultados: `df.to_csv()`, `df.to_json()`.
- Buenas prácticas: respetar robots.txt, añadir delays.

### Instrucciones

Crea un archivo `dia28.py` y escribe un programa que:

- [ ] Use `requests` y `BeautifulSoup` para scrapear datos reales de una web pública.
- [ ] Convierta los datos extraídos a un DataFrame de Pandas.
- [ ] Limpie los datos (elimine nulos, formatee precios, etc.).
- [ ] Calcule estadísticas: media, valor mínimo, valor máximo.
- [ ] Genere al menos 2 gráficos con Matplotlib.
- [ ] Exporte los resultados a CSV y JSON.

> Proyecto integrador: de la web al gráfico. ¡Todo en uno! 🏗️
