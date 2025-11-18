"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if (a== 0):
        raise ZeroDivisionError("Division by zero")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b,a)# use math library/raise ValueError

def exponent(a, b):
    return a**b



