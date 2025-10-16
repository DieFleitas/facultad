# Ejercicio 3
from typing import List


def buscar_maximo_pila(pila: List[int]) -> int:
    """
    Pre: pila no vacía.
    Busca el máximo en la pila, devolviendo el valor máximo y dejando la pila igual.
    """
    if not pila:
        raise ValueError("pila vacia")
    temp: List[int] = []
    maximo = None
    # desapilar para examinar
    while pila:
        x = pila.pop()
        temp.append(x)
        if maximo is None or x > maximo:
            maximo = x
    # restaurar
    while temp:
        pila.append(temp.pop())

    return maximo if (maximo is not None) else -1
