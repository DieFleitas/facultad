def productTable(n):
    """
    Calcula e imprime la tabla de multiplicar hasta el 10 dado un numero n
    """

    for i in range(1, 11):
        print(f"{n}*{i} = {n*i}", end="\n")