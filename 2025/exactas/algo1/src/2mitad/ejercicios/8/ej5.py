# Ejercicio 5: balanceo de paréntesis
def esta_bien_balanceada(s: str) -> bool:
    """
    Comprueba que los paréntesis en la expresión s estén bien balanceados.
    Pre: s puede contener dígitos, espacios, operadores y paréntesis.
    Post: True ssi la cantidad de '(' coincide con ')' y en todo prefijo nunca hay más ')' que '('.
    """
    pila = []
    for ch in s:
        if ch == "(":
            pila.append("(")
        elif ch == ")":
            if not pila:
                return False
            pila.pop()
        else:
            # otros caracteres los ignoramos para el balanceo
            pass
    return len(pila) == 0
