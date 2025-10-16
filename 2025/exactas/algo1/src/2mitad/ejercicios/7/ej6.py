import random


def es_matriz(m: list[list[int]]) -> bool:
    """True si m es matriz: |m|>0, |m[0]|>0 y todas las filas tienen mismo largo."""
    if len(m) == 0:
        return False
    if len(m[0]) == 0:
        return False
    ancho = len(m[0])
    i = 0
    while i < len(m):
        if len(m[i]) != ancho:
            return False
        i += 1
    return True


def filas_ordenadas(m: list[list[int]]) -> list[bool]:
    """Requiere es_matriz(m). Devuelve lista booleana por fila indicando si está ordenada (<)."""
    if not es_matriz(m):
        raise ValueError("filas_ordenadas: requiere es_matriz(m)")
    res: list[bool] = []
    i = 0
    while i < len(m):
        res.append(ordenados(m[i]))
        i += 1
    return res


def columna(m: list[list[int]], c: int) -> list[int]:
    """Requiere es_matriz(m) y 0 <= c < |m[0]|. Devuelve la columna c como lista."""
    if not es_matriz(m):
        raise ValueError("columna: requiere es_matriz(m)")
    if c < 0 or c >= len(m[0]):
        raise IndexError("columna: c fuera de rango")
    res: list[int] = []
    i = 0
    while i < len(m):
        res.append(m[i][c])
        i += 1
    return res


def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    """Requiere es_matriz(m). Devuelve booleans por columna indicando si cada columna está ordenada."""
    if not es_matriz(m):
        raise ValueError("columnas_ordenadas: requiere es_matriz(m)")
    num_cols = len(m[0])
    res: list[bool] = []
    c = 0
    while c < num_cols:
        col = columna(m, c)
        res.append(ordenados(col))
        c += 1
    return res


def transponer(m: list[list[int]]) -> list[list[int]]:
    """Requiere es_matriz(m). Devuelve la matriz transpuesta."""
    if not es_matriz(m):
        raise ValueError("transponer: requiere es_matriz(m)")
    num_rows = len(m)
    num_cols = len(m[0])
    mt: list[list[int]] = []
    c = 0
    while c < num_cols:
        # construir fila c de la transpuesta = columna c de m
        fila_c: list[int] = columna(m, c)
        mt.append(fila_c)
        c += 1
    return mt


# 6) Ta-Te-Ti Tradicional: quien_gana_tateti
def quien_gana_tateti(m: list[list[str]]) -> int:
    """
    Requiere: m es matriz 3x3 y solo contiene 'X', 'O' o ' '.
    Asegura: 0 si 'O' gana, 1 si 'X' gana, 2 si ninguno.
    Se asume que no pueden ganar ambos (precondición del enunciado).
    """
    if not es_matriz(m) or len(m) != 3 or len(m[0]) != 3:
        raise ValueError("quien_gana_tateti: requiere matriz 3x3")
    # check rows
    i = 0
    while i < 3:
        row = m[i]
        if row[0] == row[1] == row[2] and row[0] in ("X", "O"):
            return 1 if row[0] == "X" else 0
        i += 1
    # check cols
    j = 0
    while j < 3:
        a = m[0][j]
        if a == m[1][j] == m[2][j] and a in ("X", "O"):
            return 1 if a == "X" else 0
        j += 1
    # diagonals
    a = m[0][0]
    if a == m[1][1] == m[2][2] and a in ("X", "O"):
        return 1 if a == "X" else 0
    b = m[0][2]
    if b == m[1][1] == m[2][0] and b in ("X", "O"):
        return 1 if b == "X" else 0
    return 2


# Opcional: exponenciacion matriz (versión sencilla, usando int entries)
def multiplicar_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Multiplica matrices cuadradas de mismo tamaño (implementación directa)."""
    n = len(a)
    if n == 0 or len(a[0]) != n or len(b) != n or len(b[0]) != n:
        raise ValueError("multiplicar_matrices: requiere matrices cuadradas n x n")
    res: list[list[int]] = []
    i = 0
    while i < n:
        fila = []
        j = 0
        while j < n:
            # calcular res[i][j]
            s = 0
            k = 0
            while k < n:
                s += a[i][k] * b[k][j]
                k += 1
            fila.append(s)
            j += 1
        res.append(fila)
        i += 1
    return res


def exponenciacion_matriz_aleatoria(
    d: int, p: int, low: int = 0, high: int = 5
) -> list[list[int]]:
    """
    Genera una matriz dxd de enteros aleatorios en [low, high) y la eleva a p.
    Atención: esta implementación fuerza cálculo directo p veces (costosa para p grande).
    """
    if d <= 0 or p <= 0:
        raise ValueError("d y p deben ser > 0")
    # generar matriz aleatoria (enteros)
    m: list[list[int]] = []
    i = 0
    while i < d:
        fila: list[int] = []
        j = 0
        while j < d:
            fila.append(random.randint(low, high - 1))
            j += 1
        m.append(fila)
        i += 1
    # elevar a p (multiplicación repetida)
    res = m
    count = 1
    while count < p:
        res = multiplicar_matrices(res, m)
        count += 1
    return res
