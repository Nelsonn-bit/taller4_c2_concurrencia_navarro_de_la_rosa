"""
Taller 4 - Patrones Concurrentes
Autor: (Nelson Navarro de la Rosa)
Fecha: (17/11/2025)

Simula pedidos generados por productores y procesados por consumidores.

"""

import threading, queue, time, random

def productor(id_prod, cola, total_producidas):
    """Genera pedidos y los coloca en la cola compartida."""
    print(f"[Productor {id_prod}] Iniciado.")

    for i in range(10):
        
        time.sleep(random.uniform(0.3, 1.0))  # Simula E/S
        pedido = f"Pedido-{id_prod}-{i}"
        cola.put(pedido)

        print(f"[Productor {id_prod}] produjo {pedido}")
        total_producidas.append(1)  # Registrar producción

    print(f"[Productor {id_prod}] Finalizó.")


def consumidor(id_cons, cola, total_consumidas):
    """Consume pedidos de la cola y los procesa."""
    print(f"    [Consumidor {id_cons}] Iniciado.")

    while True:
        try:
            pedido = cola.get(timeout=2)
        except queue.Empty:
            break  # No más tareas

        print(f"    [Consumidor {id_cons}] procesando {pedido}")
        time.sleep(random.uniform(0.4, 1.2))  # Simula E/S

        cola.task_done()
        total_consumidas.append(1)

    print(f"    [Consumidor {id_cons}] Finalizó.")


def main():
    """Crea productores, consumidores y mide el tiempo total."""
    inicio = time.time()

    # Cola compartida
    cola = queue.Queue(maxsize=5)

    # Listas para contar tareas
    total_producidas = []
    total_consumidas = []

    # Crear hilos
    productores = [threading.Thread(target=productor, args=(i, cola, total_producidas))
                   for i in range(2)]

    consumidores = [threading.Thread(target=consumidor, args=(j, cola, total_consumidas))
                    for j in range(3)]

    # Iniciar hilos
    for h in productores + consumidores:
        h.start()

    # Esperar a que terminen
    for h in productores + consumidores:
        h.join()

    fin = time.time()

    print("\n===== RESUMEN DEL SISTEMA =====")
    print(f"Total pedidos producidos:  {len(total_producidas)}")
    print(f"Total pedidos consumidos:  {len(total_consumidas)}")
    print(f"Tiempo total de ejecución: {fin - inicio:.2f} segundos")

if __name__ == "__main__":
    main()
