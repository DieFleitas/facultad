"""
    ejercicio 2_3
"""

def fahrenheit_a_celsius(grados):
    """
        Escribir una función que convierta un valor dado en grados Fahrenheit a grados
        Celsius. Recordar que la fórmula para la conversión es: 𝐹 = 95
        𝐶 + 32
    """
    celsius = (grados - 32)*(5/9)
    print(celsius)
