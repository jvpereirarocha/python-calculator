"""
    Python operations
"""


def add(x: float, y: float) -> float:
    return x + y


def substract(x: float, y: float) -> float:
    return x - y


def divisor(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        return None


def multiply(x: float, y: float) -> float:
    return x * y
