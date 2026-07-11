# 🛠️ Python útiles para #30NitesofCode

## Estructura básica de un script

```python
#!/usr/bin/env python3


def main():
    pass


if __name__ == "__main__":
    main()
```

## Tips rápidos

| Situación | Solución |
|-----------|----------|
| Leer archivo | `with open("file.txt") as f: data = f.read()` |
| Try/except | `try: ... except Exception as e: print(e)` |
| List comprehension | `[x**2 for x in range(10)]` |
| Enumerar loop | `for i, item in enumerate(lista):` |
| Diccionario seguro | `valor = dict.get("key", default)` |

## Documentación oficial

- [Python Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [PyPI](https://pypi.org/)

## Cheatsheets

- [Python Cheatsheet](https://gto76.github.io/python-cheatsheet/)
