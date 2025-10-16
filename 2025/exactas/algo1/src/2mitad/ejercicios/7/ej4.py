def saldo_actual(movimientos: list[Tuple[str, int]]) -> int:
    """
    Pre: para cada (tipo, monto) tipo in {'I','R'} y monto > 0.
    Post: devuelve suma(ingresos) - suma(retiros).
    """
    saldo = 0
    for mov in movimientos:
        tipo, monto = mov
        if tipo not in ("I", "R"):
            raise ValueError("saldo_actual: tipo debe ser 'I' o 'R'")
        if monto <= 0:
            raise ValueError("saldo_actual: monto debe ser > 0")
        if tipo == "I":
            saldo += monto
        else:
            saldo -= monto
    return saldo
