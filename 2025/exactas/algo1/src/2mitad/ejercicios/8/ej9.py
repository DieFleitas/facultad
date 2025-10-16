# Ejercicio 9
from typing import Deque, List


def cantidad_elementos_cola(c: Deque[int]) -> int:
    """
    Cuenta elementos de la cola sin usar qsize(); deja la cola igual.
    """
    temp: List[int] = []
    contador = 0
    while c:
        x = c.popleft()
        temp.append(x)
        contador += 1
    for x in temp:
        c.append(x)
    return contador
