""" ejercicio 2-1"""

def calcular_monto_final(cantidad, tasa, anios):
    """ Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
    número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
    monto_final = cantidad * (1 + tasa/100)^anios """
    monto_final = cantidad * (1 + ((tasa / 100))**anios)
    return monto_final
