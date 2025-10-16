# Ejercicio 12: intercalar colas
from collections import deque
from typing import Deque


def intercalar_colas(c1: Deque[int], c2: Deque[int]) -> Deque[int]:
    """
    Pre: c1 y c2 tienen la misma cantidad de elementos.
    Devuelve una nueva cola con elementos intercalados y preservando el orden.
    No modifica c1 ni c2.
    """
    if len(c1) != len(c2):
        raise ValueError("c1 y c2 deben tener misma cantidad")
    res: Deque[int] = deque()
    # iterar sobre copias (no se modifica la original)
    i = 0
    n = len(c1)
    seq1 = list(c1)
    seq2 = list(c2)
    while i < n:
        res.append(seq1[i])
        res.append(seq2[i])
        i += 1
    return res
