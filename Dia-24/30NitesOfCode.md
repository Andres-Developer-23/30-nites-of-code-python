## Día 24 de #30NitesofCode 🚀

```python
# Gráficos con Matplotlib
import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie"]
temps = [22, 25, 19, 23, 27]

plt.plot(dias, temps, marker="o")
plt.title("Temperatura semanal")
plt.xlabel("Día")
plt.ylabel("°C")
plt.grid(True)
plt.show()
```

**Conceptos cubiertos:**
- `plt.plot()` — gráfico de líneas.
- `plt.bar()` — gráfico de barras.
- `plt.scatter()` — gráfico de dispersión.
- `plt.hist()` — histograma.
- `plt.pie()` — gráfico de pastel.
- Personalización: títulos, etiquetas, leyendas, colores, cuadrícula.
- `plt.subplots()` — múltiples gráficos en una figura.

### Instrucciones

Crea un archivo `dia24.py` y escribe un programa que:

- [ ] Tenga datos de temperaturas máximas y mínimas de una semana.
- [ ) Cree un gráfico de líneas con ambas series (max y min) y leyenda.
- [ ] Cree un gráfico de barras con las temperaturas máximas.
- [ ] Añada etiquetas de valor sobre cada barra.
- [ ] Guarde el gráfico como `temperaturas.png`.

> Visualizar datos es contar historias. ¡A graficar! 📈
