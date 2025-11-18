# Taller 4 – Patrones Concurrentes

Este proyecto implementa la simulación de un **sistema de procesamiento de pedidos** utilizando patrones de concurrencia en Python.  
El escenario recrea una situación real donde varios **productores** generan pedidos y los envían a una **cola compartida**, mientras múltiples **consumidores** procesan esos pedidos de forma paralela.  
El objetivo es demostrar el uso correcto de sincronización entre hilos, comunicación mediante estructuras seguras y medición del rendimiento del sistema.


Se desarrollan **dos versiones del sistema**:

---

## Versión 1 — Productores y Consumidores con hilos manuales

Los productores generan pedidos y los agregan a una cola con capacidad limitada.  
Los consumidores extraen y procesan esos pedidos de manera concurrente.  
Esta versión muestra el control manual del ciclo de vida de los hilos y la sincronización explícita entre producción y consumo.

---

## Versión 2 — Procesamiento con `ThreadPoolExecutor`

En esta implementación, los pedidos se envían como tareas al *pool* de hilos administrado por Python.  
El `ThreadPoolExecutor` gestiona automáticamente la asignación y reutilización de hilos, permitiendo observar:

- Un diseño más simple y modular.
- Mayor eficiencia en escenarios con muchas tareas.
- Diferencias claras de rendimiento frente a la versión manual.

---

Ambas versiones permiten medir el número total de pedidos procesados, el tiempo de ejecución y analizar las diferencias entre enfoques de concurrencia.

---
## Analisis de los resultados:

### 1. Flujo de trabajo concurrente

En la versión Productor–Consumidor (cola bloqueante) el flujo se organiza en roles explícitos: los productores generan elementos y los depositan en una queue.Queue, y los consumidores extraen y procesan esos elementos en paralelo. La cola actúa como buffer regulador; las operaciones put() y get() manejan el bloqueo cuando la cola está llena o vacía, lo que garantiza sincronización y evita condiciones de carrera.

En la versión con ThreadPoolExecutor el flujo es distinto: no hay productores y consumidores explícitos como hilos separados; en su lugar, se generan tareas y se envían al executor, que mantiene un pool de trabajadores reutilizables. El executor asigna automáticamente tareas a los hilos disponibles y gestiona la ejecución, por lo que la coordinación es más implícita y centrada en la entrega de tareas al pool. Esto simplifica el diseño (menos control manual del ciclo de vida de hilos) pero hace la trazabilidad del flujo un poco menos explícita comparada con la versión basada en cola.

### 2. Rendimiento comparativo

La versión con hilos manuales funciona correctamente pero presenta sobrecarga asociada a la creación y gestión explícita de hilos y a los bloqueos por cola cuando la carga es alta. 

La versión con ThreadPoolExecutor suele mostrar mejor rendimiento, ya que reutiliza hilos dentro del pool y reduce el coste de creación/destrucción de hilos, dando tiempos de ejecución más pequeños y más estables en escenarios con muchas tareas pequeñas.

### 3. Eficiencia en el uso de recursos

ThreadPoolExecutor suele ser más eficiente en CPU y memoria porque controla el número de hilos activos y reutiliza recursos. 

El patrón con cola ofrece más control y es preferible cuando las tareas llegan de forma impredecible o continua, pero escala peor ante alta carga sin una correcta configuración del pool/cola. En resumen: el ejecutor es más adecuado para alto throughput y tareas conocidas; la cola es mejor para flujos irregulares y control fino del buffer.
