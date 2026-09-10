from collections import deque
import copy

class Proceso:

    def __init__(self, nombre, tiempo, prioridad, datos):

        self.nombre = nombre
        self.tiempo_total = tiempo
        self.tiempo_restante = tiempo
        self.prioridad = prioridad
        self.datos = datos

        self.estado = "Nuevo"

    def cambiar_estado(self, nuevo_estado):

        print(f"{self.nombre}: {self.estado} -> {nuevo_estado}")
        self.estado = nuevo_estado


def mostrar_procesos(lista):

    print("\nProcesos del SIGET\n")

    print("{:<10}{:<12}{:<15}{:<15}".format(
        "Proceso",
        "Prioridad",
        "Datos(MB)",
        "CPU"
    ))

    print("-"*55)

    for p in lista:

        print("{:<10}{:<12}{:<15}{:<15}".format(
            p.nombre,
            p.prioridad,
            p.datos,
            p.tiempo_total
        ))


def round_robin(lista, quantum):

    print("\n==============================")
    print("ALGORITMO ROUND ROBIN")
    print("==============================")

    cola = deque(copy.deepcopy(lista))

    tiempo = 0

    while cola:

        proceso = cola.popleft()

        if proceso.estado == "Nuevo":
            proceso.cambiar_estado("Listo")

        proceso.cambiar_estado("En ejecución")

        ejecutar = min(quantum, proceso.tiempo_restante)

        print(f"CPU ejecutando {proceso.nombre} durante {ejecutar} unidades")

        proceso.tiempo_restante -= ejecutar

        tiempo += ejecutar

        if proceso.tiempo_restante > 0:

            proceso.cambiar_estado("Bloqueado")

            proceso.cambiar_estado("Listo")

            cola.append(proceso)

        else:

            proceso.cambiar_estado("Terminado")

    print("\nTiempo total:", tiempo)

    return tiempo


def prioridad(lista):

    print("\n==============================")
    print("ALGORITMO POR PRIORIDAD")
    print("==============================")

    procesos = sorted(copy.deepcopy(lista), key=lambda x: x.prioridad)

    tiempo = 0

    for proceso in procesos:

        proceso.cambiar_estado("Listo")

        proceso.cambiar_estado("En ejecución")

        print(f"CPU ejecutando {proceso.nombre}")

        tiempo += proceso.tiempo_total

        proceso.cambiar_estado("Terminado")

    print("\nTiempo total:", tiempo)

    return tiempo


print("="*40)
print("SIMULADOR DEL PLANIFICADOR SIGET")
print("="*40)

procesos = [

    Proceso("P1", 6, 2, 500),
    Proceso("P2", 4, 1, 250),
    Proceso("P3", 8, 3, 700)

]

mostrar_procesos(procesos)

tiempo_rr = round_robin(procesos, 2)

tiempo_pr = prioridad(procesos)

print("\n==============================")
print("COMPARACIÓN FINAL")
print("==============================")

print(f"Round Robin : {tiempo_rr}")

print(f"Prioridad   : {tiempo_pr}")

print("\nConclusión:")

print("Round Robin distribuye la CPU de manera equitativa entre todos los procesos.")

print("El algoritmo por Prioridad atiende primero las tareas críticas del SIGET, reduciendo el tiempo de respuesta para emergencias.")