# Ejercicio 7: intercalar pilas
from typing import List


def intercalar_pilas(p1: List[int], p2: List[int]) -> List[int]:
    """
    Pre: p1 y p2 tienen la misma cantidad de elementos.
    Asegura: devuelve una pila (lista) con los elementos de p1 y p2 intercalados
             preservando el orden original; el tope final es el tope de p2.
    Notación: p1, p2 bottom->top en índices 0..n-1.
    Resultado bottom->top será: p1[0], p2[0], p1[1], p2[1], ..., p1[n-1], p2[n-1]
    """
    if len(p1) != len(p2):
        raise ValueError("p1 y p2 deben tener misma cantidad")
    n = len(p1)
    res: List[int] = []
    i = 0
    while i < n:
        res.append(p1[i])
        res.append(p2[i])
        i += 1
    return res
