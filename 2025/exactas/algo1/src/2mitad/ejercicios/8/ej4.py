# Ejercicio 4
from typing import List, Tuple


def buscar_nota_maxima_pila(pila: List[Tuple[str, int]]) -> Tuple[str, int]:
    """
    Pre: pila no vacía; las segundas componentes (notas) son únicas.
    Devuelve la tupla (nombre, nota) con la nota máxima; no modifica la pila.
    """
    if not pila:
        raise ValueError("pila vacia")
    temp: List[Tuple[str, int]] = []
    mejor = None  # tipo: Tuple[str,int] | None
    while pila:
        t = pila.pop()
        temp.append(t)
        if mejor is None or t[1] > mejor[1]:
            mejor = t
    # restaurar
    while temp:
        pila.append(temp.pop())

    return mejor if (mejor is not None) else ("", -1)
