"""ejercicio 2_10"""

def imprimir_fichas(n):
    """ Modificar el programa anterior (ej2_9) para que pueda generar fichas de un juego que
    puede tener números de 0 a 𝑛."""
    for i in range(0, n):
        for j in range(i, n):
            print(f"{i} | {j}")

def main():
    """ funcion principal """
    numero = int(input("Ingrese la cantidad de fichas: "))
    imprimir_fichas(numero)

main()
