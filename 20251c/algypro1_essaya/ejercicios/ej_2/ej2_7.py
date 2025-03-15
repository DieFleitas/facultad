""" ejercicio 2_7 """

def imprimir_numeros_triangulares(numero):
    """ Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los
    primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen
    mediante la suma de los números naturales desde 1 hasta 𝑛. """
    accumulator = 0
    for i in range(numero+1):
        accumulator += i
        print(f"{i} - {accumulator}")

def imprimir_numeros_triangulares_v2(numero):
    """ Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los
    primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen
    mediante la suma de los números naturales desde 1 hasta 𝑛. """
    print(f"{numero} - {(numero*(numero+1))/2}")

def main():
    """funcion principal"""
    numero = int(input("Ingrese un numero: "))
    imprimir_numeros_triangulares(numero)

main()
