def peso_pino(altura_m: float) -> float:
    """
    Devuelve el peso estimado en kg de un pino de altura 'altura_m' metros.
    3 kg por cada centímetro hasta 3 metros (300 cm),
    2 kg por cada centímetro por encima de 3 metros.
    """
    if altura_m < 0:
        raise ValueError("altura no puede ser negativa")
    cm: float = altura_m * 100.0
    primeros_cm: float = min(cm, 300.0)
    resto_cm: float = max(cm - 300.0, 0.0)
    peso: float = primeros_cm * 3.0 + resto_cm * 2.0
    return peso


def es_peso_util(peso_kg: float) -> bool:
    """True si el peso está entre 400 y 1000 kg (inclusive)."""
    return (peso_kg >= 400.0) and (peso_kg <= 1000.0)


def sirve_pino(altura_m: float) -> bool:
    """Devuelve True si un pino de altura 'altura_m' sirve a la fábrica."""
    return es_peso_util(peso_pino(altura_m))
