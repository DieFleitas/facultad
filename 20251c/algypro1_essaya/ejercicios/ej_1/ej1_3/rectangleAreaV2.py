def calculateRectangleArea(a, b, c, d):
    """
    Calcula el area de un rectangulo alineado con los ejes x e y dadas sus cordenadas 
    x1=a, x2=b
    y1=c, y2=d
    """
    width = b - a
    height = d - c

    area = width*height

    return area