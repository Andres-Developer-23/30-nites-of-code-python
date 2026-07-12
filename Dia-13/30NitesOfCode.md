## Día 13 de #30NitesofCode 🚀

```python
# Una clase es un molde para crear objetos

class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def reproducir(self):
        return f"▶️ Sonando: {self.titulo} - {self.artista}"

c1 = Cancion("Bohemian Rhapsody", "Queen")
print(c1.reproducir())
```

**Conceptos cubiertos:**
- Clase — plantilla para crear objetos (molde).
- `__init__` — constructor, inicializa los atributos del objeto.
- `self` — referencia al propio objeto.
- Atributos — variables del objeto.
- Métodos — funciones dentro de la clase.
- Instancia — objeto creado a partir de una clase.

### Instrucciones

Crea un archivo `dia13.py` y escribe un programa que:

- [ ] Defina una clase `Libro` con atributos: título, autor, año, prestado (bool).
- [ ] Método `prestar()` que marque como prestado si no lo está.
- [ ] Método `devolver()` que marque como disponible.
- [ ] Método `info()` que muestre todos los datos.
- [ ] Cree 3 libros y simule prestar y devolver uno.

> La POO es la forma de pensar en objetos. ¡A modelar el mundo real! 🌍
