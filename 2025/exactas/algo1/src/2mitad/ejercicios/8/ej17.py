# Ejercicio 17 - historiales de navegación (pilas por usuario)
from typing import Dict, List


def visitar_sitio(historiales: Dict[str, List[str]], usuario: str, sitio: str) -> None:
    """
    Si usuario ya está en historiales añade sitio en su pila (append).
    Si no existe, crea la pila con el sitio.
    """
    if not usuario or not sitio:
        raise ValueError("usuario y sitio no vacíos")
    if usuario in historiales:
        historiales[usuario].append(sitio)
    else:
        historiales[usuario] = [sitio]


def navegar_atras(historiales: Dict[str, List[str]], usuario: str) -> str:
    """
    Quita y devuelve el tope de la pila de historial de usuario.
    Requiere usuario existente y pila no vacía.
    """
    if not usuario:
        raise ValueError("usuario no vacío")
    if usuario not in historiales:
        raise KeyError("usuario no en historiales")
    if not historiales[usuario]:
        raise ValueError("historial vacio")
    return historiales[usuario].pop()
