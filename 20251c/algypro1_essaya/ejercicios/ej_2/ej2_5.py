""" ejercicio 2_5 """

def par_o_impar(numero):
    """ a) Escribir una función que dado un número entero devuelva 1 si el mismo
    es impar y 0 si fuera par. """
    if numero % 2 == 0:
        return 0
    return 1

def par_o_impar_v2(numero):
    """ b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
    fuera par """
    if numero % 2 == 0:
        return 1
    return 0

def ultimo_digito(numero):
    """ c) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
    ejemplo, para 153 debe devolver 3. """
    return numero % 10

def ultimo_multiplo_de_diez(numero):
    """ d) Escribir una función que dado un número devuelva el primer número múltiplo de 10
    inferior a él. Por ejemplo, para 153 debe devolver 150. """
    resultado = 0
    if numero < 10:
        resultado = (numero - ultimo_digito(numero)) + 1
    resultado = numero - ultimo_digito(numero)
    return resultado
