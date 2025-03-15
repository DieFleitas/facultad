""" ejercicio 2_8"""
import ej_1.factorial

def imprimir_factorial(m):
    """ Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario,
    a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima
    el resultado junto con el número de orden correspondiente. """
    for i in range(m):
        numero = int(input("Ingrese un numero: "))
        resultado = ej_1.factorial.factorial(numero)
        print(f"{resultado} - {i}")

def main():
    """funcion principal"""
    m = int(input("Ingrese la cantidad de numeros a calcular: "))
    imprimir_factorial(m)

main()
