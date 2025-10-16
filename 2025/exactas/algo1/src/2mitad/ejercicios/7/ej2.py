# 1. CerosEnPosicionesPares (modifica s in-place)
def ceros_en_posiciones_pares_inplace(s: list[int]) -> None:
    """
    Modifica s tal que para índices pares (0,2,4,...) s[i] = 0;
    para impares conserva su valor.
    Pre: True. Modifica lista dada.
    """
    i = 0
    while i < len(s):
        if i % 2 == 0:
            s[i] = 0
        i += 1


# 2. CerosEnPosicionesPares2 (retorna nueva lista)
def ceros_en_posiciones_pares(s: list[int]) -> list[int]:
    """Devuelve nueva lista con ceros en posiciones pares."""
    res: list[int] = []
    i = 0
    while i < len(s):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(s[i])
        i += 1
    return res


# 3. sin vocales (string -> string)
def sin_vocales(s: str) -> str:
    """Quita vocales (a,e,i,o,u y mayúsculas) y concatena el resto."""
    res_chars: list[str] = []
    for ch in s:
        if ch.lower() not in ("a", "e", "i", "o", "u"):
            res_chars.append(ch)
    return "".join(res_chars)


# 4. reemplaza vocales (mismo tamaño)
def reemplaza_vocales(s: str) -> str:
    """Reemplaza cada vocal por un espacio ' ' sin cambiar longitud."""
    res_chars: list[str] = []
    for ch in s:
        if ch.lower() in ("a", "e", "i", "o", "u"):
            res_chars.append(" ")
        else:
            res_chars.append(ch)
    return "".join(res_chars)


# 5. da_vuelta_str - reverso de string
def da_vuelta_str(s: str) -> str:
    """Devuelve el reverso de s."""
    return s[::-1]


# 6. eliminar_repetidos (string -> string) preservando primera aparición
def eliminar_repetidos(s: str) -> str:
    """
    Devuelve string con caracteres únicos en el orden de primera aparición.
    Por ejemplo: 'banana' -> 'ban'.
    """
    vistos = set()
    res_chars: list[str] = []
    for ch in s:
        if ch not in vistos:
            vistos.add(ch)
            res_chars.append(ch)
    return "".join(res_chars)
