def pertenece_iter(e: int, s: list[int]) -> bool:
    """Bucle for. Pre: True. Post: True iff existe i tal que s[i] == e."""
    for x in s:
        if x == e:
            return True
    return False


def pertenece_while(e: int, s: list[int]) -> bool:
    """Bucle while. Pre: True."""
    i = 0
    n = len(s)
    while i < n:
        if s[i] == e:
            return True
        i += 1
    return False


def pertenece_in(e: int, s: list[int]) -> bool:
    """Usa operador 'in' de Python (forma idiomática)."""
    return e in s


# 2. divide a todos (e != 0)
def divide_a_todos(e: int, s: list[int]) -> bool:
    """Pre: e != 0. Post: True iff todos los elementos de s son divisibles por e."""
    if e == 0:
        raise ValueError("divide_a_todos: e no puede ser 0")
    for x in s:
        if x % e != 0:
            return False
    return True


# 3. suma total (no usar sum())
def suma_total(s: list[int]) -> int:
    """Pre: True. Post: suma de los elementos. No usar sum()."""
    acc = 0
    for x in s:
        acc += x
    return acc


# 4. maximo (no usar max())
def maximo(s: list[int]) -> int:
    """Pre: |s| > 0. Post: máximo de s."""
    if len(s) == 0:
        raise ValueError("maximo: lista vacía")
    m = s[0]
    for x in s[1:]:
        if x > m:
            m = x
    return m


# 5. minimo (no usar min())
def minimo(s: list[int]) -> int:
    """Pre: |s| > 0. Post: mínimo de s."""
    if len(s) == 0:
        raise ValueError("minimo: lista vacía")
    m = s[0]
    for x in s[1:]:
        if x < m:
            m = x
    return m


# 6. ordenados (estrictamente creciente)
def ordenados(s: list[int]) -> bool:
    """Pre: True. Post: True iff s[i] < s[i+1] para todo i."""
    n = len(s)
    i = 0
    while i + 1 < n:
        if not (s[i] < s[i + 1]):
            return False
        i += 1
    return True


# 7. pos_maximo: -1 si vacía; si varios, primera aparición
def pos_maximo(s: list[int]) -> int:
    """Pre: True. Post: índice (primer) del máximo o -1 si vacío."""
    if len(s) == 0:
        return -1
    pos = 0
    m = s[0]
    i = 1
    while i < len(s):
        if s[i] > m:
            m = s[i]
            pos = i
        i += 1
    return pos


# 8. pos_minimo: -1 si vacía; si varios, la última aparición
def pos_minimo(s: list[int]) -> int:
    """Pre: True. Post: índice de la última aparición del mínimo, o -1 si vacío."""
    if len(s) == 0:
        return -1
    pos = 0
    m = s[0]
    i = 0
    while i < len(s):
        if s[i] < m:
            m = s[i]
            pos = i
        elif s[i] == m:
            pos = i  # actualizar para quedar con la última aparición
        i += 1
    return pos


# 9. long mayorASiete (lista de palabras)
def long_mayorASiete(s: list[str]) -> bool:
    """Pre: True. Post: True si alguna palabra tiene longitud > 7."""
    for w in s:
        if len(w) > 7:
            return True
    return False


# 10. es_palindroma (string)
def es_palindroma(s: str) -> bool:
    """Pre: True. Post: True si s == reversed(s). Cadenas vacías o len 1 son palíndromas."""
    return s == s[::-1]


# 11. iguales_consecutivos: 3 iguales consecutivos
def iguales_consecutivos(s: list[int]) -> bool:
    """Pre: True. Post: True si existe i tal que s[i] == s[i+1] == s[i+2]."""
    n = len(s)
    i = 0
    while i + 2 < n:
        if s[i] == s[i + 1] == s[i + 2]:
            return True
        i += 1
    return False


# 12. vocales distintas en una palabra (al menos 3 distintas)
def vocales_distintas(s: str) -> bool:
    """Pre: True. Post: True si al menos 3 vocales distintas (a,e,i,o,u) aparecen en s."""
    vocales = set()
    for ch in s:
        c = ch.lower()
        if c in ("a", "e", "i", "o", "u"):
            vocales.add(c)
            if len(vocales) >= 3:
                return True
    return False


# 13. pos_secuencia_ordenada_mas_larga (subsecuencia contigua no decreciente)
def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    """
    Pre: |s| > 0.
    Post: devuelve i donde inicia la secuencia ordenada (no decreciente) mas larga.
    Si empate, devuelve la primera.
    """
    n = len(s)
    best_start = 0
    best_len = 1
    cur_start = 0
    cur_len = 1
    i = 1
    while i < n:
        if s[i - 1] <= s[i]:
            cur_len += 1
        else:
            # cerrar actual
            if cur_len > best_len:
                best_len = cur_len
                best_start = cur_start
            cur_start = i
            cur_len = 1
        i += 1
    # comparar al final
    if cur_len > best_len:
        best_len = cur_len
        best_start = cur_start
    return best_start


# 14. cantidad digitos impares (todos los elementos >= 0)
def cantidad_digitos_impares(nums: list[int]) -> int:
    """
    Pre: todos los elementos >= 0.
    Post: número total de dígitos impares en la representación decimal de todos los números.
    """
    total = 0
    for num in nums:
        if num == 0:
            # 0 no contribuye porque 0 es par
            continue
        x = num
        while x > 0:
            d = x % 10
            if d % 2 == 1:
                total += 1
            x = x // 10
    return total
