def imprimir_1_a_10() -> None:
    i: int = 1
    while i <= 10:
        print(i)
        i += 1


def imprimir_pares_10_40() -> None:
    n: int = 10
    while n <= 40:
        if n % 2 == 0:
            print(n)
        n += 1
    # alternativa: iniciar en 10 y aumentar en 2: n=10; while n<=40: print(n); n+=2


def imprimir_eco_10_veces() -> None:
    contador: int = 0
    while contador < 10:
        print("eco")
        contador += 1


def cuenta_regresiva(n: int) -> None:
    """
    Imprime desde n hasta 1 y al final 'Despegue'.
    Requiere n > 0.
    """
    if n <= 0:
        raise ValueError("n debe ser positivo")
    while n >= 1:
        print(n)
        n -= 1
    print("Despegue")


def viaje_en_el_tiempo(anio_partida: int, anio_llegada: int) -> None:
    """
    Viaja de anio_partida hacia anio_llegada (anio_llegada < anio_partida),
    saltando de a 1 año y mostrando mensaje por cada salto.
    """
    if anio_llegada >= anio_partida:
        raise ValueError("anio_llegada debe ser menor que anio_partida")
    actual: int = anio_partida
    while actual > anio_llegada:
        actual -= 1
        print(f"Viajó un año al pasado, estamos en el año: {actual}")


def viaje_rapido_hasta_aristoteles(anio_partida: int) -> None:
    """
    Viaja desde anio_partida hacia el pasado en pasos de 20 años hasta llegar
    al año más cercano que sea <= -384 (384 a.C.), imprimiendo mensaje por salto.
    """
    target: int = -384
    actual: int = anio_partida
    if actual <= target:
        print("Ya estamos en o antes de -384.")
        return
    while actual > target:
        actual -= 20
        # si pasamos por debajo de target, ajustamos al target para el mensaje final
        if actual < target:
            actual = target
        print(f"Viajó 20 años al pasado, estamos en el año: {actual}")
