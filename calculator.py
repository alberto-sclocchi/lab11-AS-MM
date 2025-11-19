"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")

        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def hypotenuse(a,b):
    try:
        return math.hypot(a,b)
    except Exception as e:
        print(f"Error: {e}")
        return None

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b,a)# use math library/raise ValueError

def exponent(a, b):
    return a**b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return a / b
    return b / a # raise ZeroDivisionError if a == 0

