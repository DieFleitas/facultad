# Ejercicio 6: evaluación de expresiones en notación postfix
import re
from typing import List


def evaluar_expresion_postfix(s: str) -> float:
    """
    Evalúa una expresión en notación postfix con tokens separados por un único espacio.
    Operandos enteros; operadores binarios +, -, *, /.
    Devuelve resultado float (uso división real).
    Pre: expresión sintácticamente válida.
    """
    if not s:
        raise ValueError("expresión vacía")
    stack: List[float] = []
    tokens = s.split(" ")
    for token in tokens:
        token = token.strip()
        if token == "":
            continue
        if re.fullmatch(r"-?\d+", token):
            stack.append(float(int(token)))
        elif token in ("+", "-", "*", "/"):
            if len(stack) < 2:
                raise ValueError(
                    "expresión inválida: operador con operandos insuficientes"
                )
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("división por cero en expresión")
                stack.append(a / b)
        else:
            raise ValueError(f"token inválido: {token}")
    if len(stack) != 1:
        raise ValueError("expresión inválida: quedan elementos en la pila")
    return stack[0]
