# Ejercicio 2
from typing import List


def cantidad_elementos_pila(pila: List[int]) -> int:
    """
    Cuenta la cantidad de elementos de la pila sin usar len() como único medio conceptual.
    Recorre y restaura la pila (la deja igual al final).
    """
    temp: List[int] = []
    contador = 0
    # desapilar todo contando
    while pila:
        temp.append(pila.pop())
        contador += 1
    # restaurar en mismo orden
    while temp:
        pila.append(temp.pop())
    return contador
