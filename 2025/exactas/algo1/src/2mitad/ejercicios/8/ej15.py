# Ejercicio 15 - atención de clientes en banco
from collections import deque
from typing import Deque, List, Tuple


def atencion_a_clientes(
    c: Deque[Tuple[str, int, bool, bool]],
) -> Deque[Tuple[str, int, bool, bool]]:
    """
    c: cola de (nombre, dni, cuenta_preferencial: bool, tiene_prioridad: bool)
    Regla de atención: primero quienes tienen prioridad (tiene_prioridad True), luego cuenta preferencial,
    luego resto. Dentro de cada grupo se respeta orden de llegada.
    Devuelve nueva cola ordenada según la política.
    """
    prioridad: List[Tuple[str, int, bool, bool]] = []
    preferencial: List[Tuple[str, int, bool, bool]] = []
    resto: List[Tuple[str, int, bool, bool]] = []
    for cliente in c:
        _, _, es_pref, tiene_prior = cliente
        if tiene_prior:
            prioridad.append(cliente)
        elif es_pref:
            preferencial.append(cliente)
        else:
            resto.append(cliente)
    res = deque()
    for grupo in (prioridad, preferencial, resto):
        for cliente in grupo:
            res.append(cliente)
    return res
