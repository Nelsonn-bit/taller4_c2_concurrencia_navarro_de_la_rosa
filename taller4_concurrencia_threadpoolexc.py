"""
Taller 4 Versión 2
Procesamiento concurrente usando ThreadPoolExecutor.

Simula la ejecución de pedidos con un pool de hilos
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time, random

def procesar_pedido(nombre):
    """
    Simula el procesamiento de un pedido mediante una pausa aleatoria.
    """
    duracion = random.uniform(0.4, 1.2)
    print(f"[{nombre}] iniciado (duración {duracion:.2f}s)")
    time.sleep(duracion)
    return f"{nombre} completado"


def main():
    """
    Crea un conjunto de tareas y las procesa concurrentemente con un thread pool.
    Mide el tiempo total de ejecución.
    """
    inicio = time.time()

    # Generar pedidos (similar cantidad que en versión 1)
    pedidos = [f"Pedido-{i}" for i in range(10)]

    print(f"\n=== VERSIÓN 2: ThreadPoolExecutor con {len(pedidos)} tareas ===")

    resultados = []

    # Pool de hilos (3 como los consumidores)
    with ThreadPoolExecutor(max_workers=3) as executor:
        futuros = [executor.submit(procesar_pedido, p) for p in pedidos]

        for futuro in as_completed(futuros):
            resultados.append(futuro.result())

    fin = time.time()

    
    print("\n===== RESUMEN DEL SISTEMA =====")
    print(f"Total de pedidos procesados: {len(resultados)}")

    print("Resultados:")
    for r in resultados:
        print("  ->", r)

    print(f"Tiempo total de ejecución: {fin - inicio:.2f} segundos")


if __name__ == "__main__":
    main()
