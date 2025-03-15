""" ejercicio 2_6 """
from ej2_5 import par_o_impar

def imprimir_pares(inicio, final):
    """ Escribir un programa que imprima todos los números pares entre dos números
    que se le pidan al usuario. """
    for i in range(inicio, final+1):
        if par_o_impar(i) == 0:
            print(i)


def main():
    """ funcion principal """
    inicio = int(input("Ingrese el valor de inicio: "))
    final = int(input("Ingrese el valor de fin: "))
    imprimir_pares(inicio, final)

main()
