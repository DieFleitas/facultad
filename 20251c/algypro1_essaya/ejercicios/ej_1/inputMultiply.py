from multiply import *

def inputMultiply():
    """
    Le pide dos valores al usuario y devuelve su producto
    """
    x = int(input("Ingrese un número: "))
    y = int(input("Ingrese otro número: "))

    print(multiply(x, y))
