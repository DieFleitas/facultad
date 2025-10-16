# Ejercicio 18 - inventario
from typing import Dict, Union


ProductInfo = Dict[str, Union[int, float]]  # {'precio': float, 'cantidad': int}


def agregar_producto(
    inventario: Dict[str, ProductInfo], nombre: str, precio: float, cantidad: int
) -> None:
    if not nombre:
        raise ValueError("nombre no vacio")
    if precio < 0 or cantidad < 0:
        raise ValueError("precio y cantidad >= 0")
    if nombre in inventario:
        raise KeyError("producto ya existe")
    inventario[nombre] = {"precio": float(precio), "cantidad": int(cantidad)}


def actualizar_stock(
    inventario: Dict[str, ProductInfo], nombre: str, cantidad: int
) -> None:
    if not nombre:
        raise ValueError("nombre no vacio")
    if cantidad < 0:
        raise ValueError("cantidad >= 0")
    if nombre not in inventario:
        raise KeyError("producto no existe")
    inventario[nombre]["cantidad"] = int(cantidad)


def actualizar_precio(
    inventario: Dict[str, ProductInfo], nombre: str, precio: float
) -> None:
    if not nombre:
        raise ValueError("nombre no vacio")
    if precio < 0:
        raise ValueError("precio >= 0")
    if nombre not in inventario:
        raise KeyError("producto no existe")
    inventario[nombre]["precio"] = float(precio)


def calcular_valor_inventario(inventario: Dict[str, ProductInfo]) -> float:
    total = 0.0
    for nombre, info in inventario.items():
        if not nombre:
            raise ValueError("clave vacia en inventario")
        precio = float(info.get("precio", 0.0))
        cantidad = int(info.get("cantidad", 0))
        total += precio * cantidad
    return total
