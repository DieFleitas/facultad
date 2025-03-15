"""
    ejercicio 2_2
"""
from ej2_1 import calcular_monto_final

def obtener_monto():
    """
        Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
        al usuario la cantidad de pesos inicial, la tasa de interés 
        y el número de años y muestre el monto final a obtener.
    """
    cantidad = int(input("Ingrese cantidad inicial: "))
    tasa = int(input("Ingrese tasa de interes: "))
    anios = int(input("Ingrese el plazo en años: "))
    monto = calcular_monto_final(cantidad, tasa, anios)
    print(monto)

def main():
    """
        función principal
    """
    obtener_monto()
    return

main()
