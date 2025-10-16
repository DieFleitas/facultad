def devolver_el_doble_si_es_par(numero: int) -> int:
    """Si numero es par devuelve el doble, sino devuelve el numero."""
    if es_par(numero):
        return 2 * numero
    else:
        return numero


def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if es_par(numero):
        return numero
    else:
        return numero + 1


def devolver_valor_si_es_par_sino_el_que_sigue_dos_if(numero: int) -> int:
    if es_par(numero):
        return numero
    if not es_par(numero):
        return numero + 1


def devolver_doble_o_triple(numero: int) -> int:
    """
    Si numero múltiplo de 9 -> devuelve 3*numero.
    Else si múltiplo de 3 -> devuelve 2*numero.
    Else -> devuelve numero.
    """
    if es_multiplo_de(numero, 9):
        return 3 * numero
    elif es_multiplo_de(numero, 3):
        return 2 * numero
    else:
        return numero


def lindo_nombre(nombre: str) -> None:
    """Imprime un mensaje según la longitud del nombre."""
    if len(nombre) >= 5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")


def elRango(numero: int) -> None:
    """Imprime el intervalo donde cae 'numero' según la especificación."""
    if numero < 5:
        print("Menor a 5")
    elif 10 <= numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")
    else:
        # cubre 5..9
        print("Entre 5 y 9")


def destino_segun_sexo_y_edad(sexo: str, edad: int) -> None:
    """
    Imprime 'Andá de vacaciones' si corresponde (menor de 18 o jubilado segun sexo),
    sino 'Te toca trabajar'.
    sexo debe ser 'F' o 'M' (mayúsculas).
    """
    if sexo not in ("F", "M"):
        raise ValueError("sexo debe ser 'F' o 'M'")
    if edad < 0:
        raise ValueError("edad no puede ser negativa")

    # umbral de jubilacion según sexo
    if sexo == "F":
        umbral = 60
    else:
        umbral = 65

    if edad < 18 or edad >= umbral:
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")
