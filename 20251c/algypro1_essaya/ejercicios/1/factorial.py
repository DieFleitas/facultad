def factorial(n):
    """
    Calcula el factorial del numero n
    """

    result = 1
    for x in range(1, n+1):
        result = result * x

    return result