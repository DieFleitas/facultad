def resultado_materia(notas: list[int]) -> int:
    """
    Pre: |notas| > 0; 0 <= notas[i] <= 10.
    Post:
      res = 1 iff todos >= 4 and promedio >= 7
      res = 2 iff todos >= 4 and 4 <= promedio < 7
      res = 3 iff alguno < 4 or promedio < 4
    """
    if len(notas) == 0:
        raise ValueError("resultado_materia: debe haber al menos una nota")
    for nt in notas:
        if nt < 0 or nt > 10:
            raise ValueError("resultado_materia: notas deben estar entre 0 y 10")
    total = 0
    for nt in notas:
        total += nt
    promedio = total / len(notas)
    todos_ge4 = True
    for nt in notas:
        if nt < 4:
            todos_ge4 = False
            break
    if todos_ge4 and promedio >= 7.0:
        return 1
    if todos_ge4 and 4.0 <= promedio < 7.0:
        return 2
    # si alguno <4 o promedio <4
    return 3
