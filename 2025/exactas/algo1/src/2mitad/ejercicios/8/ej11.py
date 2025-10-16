# Ejercicio 11
from typing import Deque, List, Tuple


def buscar_nota_minima_cola(c: Deque[Tuple[str, int]]) -> Tuple[str, int]:
    """
    Pre: cola no vacía; notas únicas en segunda componente.
    Devuelve la tupla con nota mínima; deja la cola igual.
    """
    if not c:
        raise ValueError("cola vacia")
    temp: List[Tuple[str, int]] = []
    minimo = None
    while c:
        t = c.popleft()
        temp.append(t)
        if minimo is None or t[1] < minimo[1]:
            minimo = t
    for t in temp:
        c.append(t)
    return minimo if (minimo is not None) else ("", -1)
