import math


def imprimir_saludo(nombre: str) -> None:
    """Imprime 'Hola <nombre>'."""
    print(f"Hola {nombre}")


def raiz_cuadrada_de(numero: float) -> float:
    """Devuelve la raiz cuadrada de 'numero'. Requiere numero >= 0 si se usa
    math.sqrt."""
    if numero < 0:
        raise ValueError("numero debe ser >= 0")
    return math.sqrt(numero)


def fahrenheit_a_celsius(t: float) -> float:
    """Convierte grados Fahrenheit a Celsius usando la fórmula ((t-32)*5)/9."""
    return ((t - 32) * 5) / 9


def imprimir_dos_veces(estribillo: str) -> None:
    """Imprime el estribillo dos veces (cada repetición en su propia línea)."""
    print(estribillo)
    print(estribillo)
    # alternativa usando repetición y splitlines:
    # print((estribillo + "\n") * 2, end="")


def es_multiplo_de(n: int, m: int) -> bool:
    """Devuelve True si n es múltiplo de m. Requiere m != 0."""
    if m == 0:
        raise ValueError("m no puede ser 0")
    return n % m == 0


def es_par(numero: int) -> bool:
    """Devuelve True si numero es par, usando es_multiplo_de."""
    return es_multiplo_de(numero, 2)


def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    """
    Devuelve la cantidad de pizzas necesarias para que cada comensal coma al
    menos
    min_cant_de_porciones porciones. Cada pizza tiene 8 porciones.
    """
    if comensales < 0 or min_cant_de_porciones < 0:
        raise ValueError("valores no negativos")
    porciones_por_persona: int = min_cant_de_porciones
    total_porciones_necesarias: int = comensales * porciones_por_persona
    pizzas: int = math.ceil(total_porciones_necesarias / 8)
    return pizzas
