# Ejercicio 14 - pacientes urgentes
from typing import Deque, Tuple


def pacientes_urgentes(c: Deque[Tuple[int, str, str]]) -> int:
    """
    c: cola de tuplas (prioridad: 1..10, nombre, especialidad)
    Devuelve la cantidad con prioridad < 4.
    """
    count = 0
    for item in c:
        prio = item[0]
        if prio < 4:
            count += 1
    return count
