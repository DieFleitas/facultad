"""
    ejercicio 2_4
"""
from ej2_3 import fahrenheit_a_celsius

def obtener_grados_celsius():
    """
        Escribir un programa que utilice la función anterior para generar una tabla de
        conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
    """
    for i in range(0, 121, 10):
        print(fahrenheit_a_celsius(i))

def main():
    """ funcion principal """
    obtener_grados_celsius()
