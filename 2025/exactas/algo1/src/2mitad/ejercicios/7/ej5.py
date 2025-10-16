# Reutilizamos pertenece_in/while/iter para listas internas.


def pertenece_a_cada_uno_v1(s: list[list[int]], e: int, res: list[bool]) -> None:
    """
    Version 1: out res (modifica lista res dada). Se requiere: |res| >= |s|.
    Asegura: para 0 <= i < |s|, res[i] = (e in s[i]).
    """
    if len(res) < len(s):
        # agrandar res rellenando con False para cumplir |res| >= |s|
        idx = len(res)
        while idx < len(s):
            res.append(False)
            idx += 1
    i = 0
    while i < len(s):
        res[i] = e in s[i]
        i += 1
    # Si res era más larga, dejamos el resto sin tocar (es compatible con |res| >= |s|)


def pertenece_a_cada_uno_v2(s: list[list[int]], e: int, res: list[bool]) -> None:
    """
    Version 2: out res (modifica) pero exige |res| == |s|.
    Si |res| != |s| raise error (para respetar la especificación).
    """
    if len(res) != len(s):
        raise ValueError("pertenece_a_cada_uno_v2: |res| debe ser igual a |s|")
    i = 0
    while i < len(s):
        res[i] = e in s[i]
        i += 1


def pertenece_a_cada_uno_v3(s: list[list[int]], e: int) -> list[bool]:
    """
    Version 3: retorna lista de booleans de longitud |s| con la propiedad pedida.
    """
    res: list[bool] = []
    i = 0
    while i < len(s):
        res.append(e in s[i])
        i += 1
    return res


# Comentario sobre diferencias:
# - v1 permite una lista "res" ya existente más larga (|res| >= |s|) y la completa (modifica).
# - v2 exige exactamente el mismo tamaño y lo escribe.
# - v3 simplemente devuelve la lista resultante.
# En términos de fuerza: v2 es más exigente en la entrada (|res| debe ser exactamente |s|),
# v1 es la más laxa en este aspecto; v3 es la más natural desde Python (no requiere res previa).
