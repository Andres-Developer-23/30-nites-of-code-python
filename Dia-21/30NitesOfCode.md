## Día 21 de #30NitesofCode 🚀

```python
# Dos hilos ejecutándose "al mismo tiempo"
import threading
import time

def tarea(nombre, segundos):
    print(f"  {nombre} inicia")
    time.sleep(segundos)
    print(f"  {nombre} termina")

hilo1 = threading.Thread(target=tarea, args=("A", 2))
hilo2 = threading.Thread(target=tarea, args=("B", 2))
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("✅ Ambos hilos terminaron")
```

**Conceptos cubiertos:**
- `threading.Thread(target=func, args=())` — crear un hilo.
- `.start()` — inicia el hilo.
- `.join()` — espera a que el hilo termine.
- Diferencia: `threading` (I/O bound) vs `multiprocessing` (CPU bound).
- GIL (Global Interpreter Lock).
- `concurrent.futures` — `ThreadPoolExecutor`, `ProcessPoolExecutor`.

### Instrucciones

Crea un archivo `dia21.py` y escribe un programa que:

- [ ] Tenga una lista de 5 URLs de sitios web.
- [ ] Use `ThreadPoolExecutor` para descargar el HTML de cada una en paralelo.
- [ ] Mida el tiempo total (con y sin hilos).
- [ ] Muestre el tamaño en bytes de cada página descargada.

> Concurrencia: haz más cosas al mismo tiempo. ¡A paralelizar! ⚡
