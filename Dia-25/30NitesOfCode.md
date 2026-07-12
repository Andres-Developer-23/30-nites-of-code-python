## Día 25 de #30NitesofCode 🚀

```python
# Extraer información de páginas web
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

citas = soup.find_all("span", class_="text")
for cita in citas[:3]:
    print(cita.get_text())
```

**Conceptos cubiertos:**
- `requests.get()` — descarga el HTML de una página.
- `BeautifulSoup(html, "html.parser")` — parsea el HTML.
- `soup.find_all("tag", class_="clase")` — busca elementos.
- `soup.find("tag", id="id")` — busca el primer elemento.
- `.get_text()` — obtiene el texto del elemento.
- `.get("atributo")` — obtiene un atributo (href, src, etc.).

### Instrucciones

Crea un archivo `dia25.py` y escribe un programa que:

- [ ) Extraiga los titulares de noticias de `https://news.ycombinator.com/`.
- [ ] Extraiga los enlaces (href) de cada titular.
- [ ] Muestre los primeros 10 titulares numerados.
- [ ] Guarde los resultados en un archivo `noticias.txt`.

> Web scraping: el mundo es tu base de datos. ¡A extraer! 🕸️
