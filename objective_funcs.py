"""
objective_funcs.py
Morgan Bauer
22 February 2024

Homework 01 for CS-470 Evolutionary Computation
Defines objective functions that can be used in the SGA implementation in sga.py
pledged
"""
from math import sin, cos

def objective_func_1(x: int, c: int, n: int) -> float:
    """Maximum is 1.0"""
    if x < 0 or x > c:
        raise ValueError("x does not belong to the domain")

    if type(x) != int:
        raise TypeError("x must be an integer")

    if type(c) != int:
        raise TypeError("c must be an integer")

    if type(n) != int:
        raise TypeError("n must be an integer")
    return (x / c) ** n

def objective_func_2(x: int, c: int, n: int) -> float:
    """Maximum is approximately 0.839"""
    if x < 0 or x > c:
        raise ValueError("x does not belong to the domain")
    if type(x) != int:
        raise TypeError("x must be an integer")
    if type(c) != int:
        raise TypeError("c must be an integer")
    f_x = (-((112 / 3) * ((x / c) ** 4))) + (72 * ((x / c) ** 3))\
          - ((131 / 3) * ((x / c) ** 2)) + (9 * (x / c))
    return f_x

def objective_func_3(x: int, c: int, n: int) -> float:
    """Maximum is approximately 2.598"""
    if x < 0 or x > c:
        raise ValueError("x does not belong to the domain")
    if type(x) != int:
        raise TypeError("x must be an integer")
    if type(c) != int:
        raise TypeError("c must be an integer")
    return 2 * cos(x / c) + sin(2 * (x / c))