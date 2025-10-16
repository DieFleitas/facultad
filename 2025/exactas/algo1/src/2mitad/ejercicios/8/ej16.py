# Ejercicio 16
from typing import Dict, List, Tuple


def calcular_promedio_por_estudiante(
    notas: List[Tuple[str, float]],
) -> Dict[str, float]:
    """
    Input: lista de pares (nombre, nota).
    Output: diccionario nombre -> promedio de sus notas.
    """
    sums: Dict[str, float] = {}
    counts: Dict[str, int] = {}
    for nombre, nota in notas:
        if nombre == "":
            raise ValueError("nombre no puede ser vacío")
        if nota < 0 or nota > 10:
            raise ValueError("nota fuera de rango")
        sums[nombre] = sums.get(nombre, 0.0) + nota
        counts[nombre] = counts.get(nombre, 0) + 1
    res: Dict[str, float] = {}
    for nombre in sums:
        res[nombre] = sums[nombre] / counts[nombre]
    return res
