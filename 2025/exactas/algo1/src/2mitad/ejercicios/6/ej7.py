def imprimir_1_a_10_for() -> None:
    for i in range(1, 11):
        print(i)


def imprimir_pares_10_40_for() -> None:
    for n in range(10, 41, 2):
        print(n)


def imprimir_eco_10_veces_for() -> None:
    for _ in range(10):
        print("eco")


def cuenta_regresiva_for(n: int) -> None:
    if n <= 0:
        raise ValueError("n debe ser positivo")
    for i in range(n, 0, -1):
        print(i)
    print("Despegue")


def viaje_en_el_tiempo_for(anio_partida: int, anio_llegada: int) -> None:
    if anio_llegada >= anio_partida:
        raise ValueError("anio_llegada debe ser menor que anio_partida")
    # range(start-1, anio_llegada-1, -1) para obtener los años visitados
    for año in range(anio_partida - 1, anio_llegada - 1, -1):
        print(f"Viajó un año al pasado, estamos en el año: {año}")


def viaje_rapido_hasta_aristoteles_for(anio_partida: int) -> None:
    target: int = -384
    if anio_partida <= target:
        print("Ya estamos en o antes de -384.")
        return
    # calculamos el primer año recorrido: anio_partida - 20, y usamos range hasta target inclusive
    año = anio_partida - 20
    while año > target:
        print(f"Viajó 20 años al pasado, estamos en el año: {año}")
        año -= 20
    # si el ultimo salto pasó por debajo, ajustamos
    if año <= target:
        print(f"Viajó 20 años al pasado, estamos en el año: {target}")
