# Ejercicio 10
from typing import Deque, List


def buscar_maximo_cola(c: Deque[int]) -> int:
    """
    Pre: cola no vacía. Devuelve el máximo entre los elementos; deja la cola igual.
    """
    if not c:
        raise ValueError("cola vacia")
    temp: List[int] = []
    maximo = None
    while c:
        x = c.popleft()
        temp.append(x)
        if maximo is None or x > maximo:
            maximo = x
    for x in temp:
        c.append(x)
    return maximo if (maximo is not None) else -1
