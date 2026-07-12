## Día 14 de #30NitesofCode 🚀

```python
# Herencia: una clase puede extender otra

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "..."

class Perro(Animal):
    def sonido(self):
        return "¡Guau! 🐕"

class Gato(Animal):
    def sonido(self):
        return "¡Miau! 🐱"

animales = [Perro("Max"), Gato("Luna")]
for a in animales:
    print(f"{a.nombre}: {a.sonido()}")
```

**Conceptos cubiertos:**
- Herencia: `class Hija(Padre)`.
- `super().__init__()` — llama al constructor de la clase padre.
- Sobrescritura de métodos.
- Polimorfismo — mismos métodos con diferentes comportamientos.
- Métodos especiales: `__str__`, `__repr__`, `__len__`, `__eq__`.

### Instrucciones

Crea un archivo `dia14.py` y escribe un programa que:

- [ ] Defina una clase `Empleado` con nombre, salario_base.
- [ ] Defina `Desarrollador(Empleado)` que agregue `lenguaje` y bonifique +20%.
- [ ] Defina `Gerente(Empleado)` que agregue `departamento` y bonifique +30%.
- [ ] Cree 2 desarrolladores y 1 gerente.
- [ ] Muestre el salario de cada uno después de la bonificación.

> Herencia: no reinventes la rueda, extiéndela. ¡A reutilizar! ♻️
