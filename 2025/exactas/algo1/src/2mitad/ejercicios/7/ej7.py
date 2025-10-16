# 1) Construir lista de nombres hasta 'listo' o entrada vacía
def leer_nombres() -> list[str]:
    """
    Pide nombres al usuario hasta que ingrese 'listo' (cualquier caso) o cadena vacía.
    Devuelve lista con los nombres ingresados (sin 'listo').
    """
    nombres: list[str] = []
    while True:
        entrada = input("Ingrese nombre (ENTER o 'listo' para terminar): ").strip()
        if entrada == "" or entrada.lower() == "listo":
            break
        nombres.append(entrada)
    return nombres


# 2) Historial monedero (SUBE) interactivo
def simulador_monedero() -> list[Tuple[str, int]]:
    """
    Interactivo:
    - 'C' cargar créditos
    - 'D' descontar créditos
    - 'X' finalizar
    Devuelve el historial como lista de tuplas (tipo,monto).
    """
    historial: list[Tuple[str, int]] = []
    while True:
        accion = (
            input("Ingrese acción (C= Cargar, D=Descontar, X=Salir): ").strip().upper()
        )
        if accion == "X":
            break
        if accion not in ("C", "D"):
            print("Acción inválida. Intente nuevamente.")
            continue
        try:
            monto_str = input("Ingrese monto (entero positivo): ").strip()
            monto = int(monto_str)
            if monto <= 0:
                print("Monto debe ser > 0.")
                continue
        except ValueError:
            print("Monto inválido.")
            continue
        historial.append((accion, monto))
    return historial


# 3) Juego 7 y medio (simulación interactiva)
def jugar_siete_y_medio() -> list[int]:
    """
    Genera cartas aleatorias entre 1 y 12 excluyendo 8 y 9.
    Figuras 10/11/12 valen 0.5. Suma acumulada; si > 7.5 pierde.
    Pregunta al usuario si quiere otra carta ('s' para sí, otra para no).
    Devuelve historial de cartas (lista de enteros).
    """
    historial: list[int] = []
    total = 0.0
    print("Comienza juego 7 y medio.")
    while True:
        # obtener carta aleatoria excluyendo 8 y 9
        carta = random.randint(1, 12)
        while carta in (8, 9):
            carta = random.randint(1, 12)
        historial.append(carta)
        if carta in (10, 11, 12):
            valor = 0.5
            print(f"Salió figura {carta} -> vale 0.5")
        else:
            valor = float(carta)
            print(f"Salió {carta} -> vale {valor}")
        total += valor
        print(f"Total acumulado: {total}")
        if total > 7.5:
            print("Te pasaste. Perdiste.")
            break
        seguir = (
            input("¿Querés otra carta? (s para sí, otra para plantarse): ")
            .strip()
            .lower()
        )
        if seguir != "s":
            print("Te plantaste. Fin de la mano.")
            break
    return historial


# 4) Fortaleza de contraseña
def analizar_contrasena(pw: str) -> str:
    """
    Devuelve 'VERDE' si cumple:
      - longitud > 8
      - al menos una minúscula
      - al menos una mayúscula
      - al menos un dígito
    Devuelve 'ROJA' si longitud < 5.
    En otro caso devuelve 'AMARILLA'.
    """
    if len(pw) < 5:
        return "ROJA"
    tiene_minus = False
    tiene_mayus = False
    tiene_digito = False
    for ch in pw:
        if "a" <= ch <= "z":
            tiene_minus = True
        elif "A" <= ch <= "Z":
            tiene_mayus = True
        elif "0" <= ch <= "9":
            tiene_digito = True
    if len(pw) > 8 and tiene_minus and tiene_mayus and tiene_digito:
        return "VERDE"
    return "AMARILLA"
