"""
Course: ITSC 3155
Purpose: The calculator class is meant to do basic arithmetic. Every method
takes two int parameters and can compute the four basic arithmetic operations
add, subtract, multiplye and divide.
Author: Ranvita Kothapalli
"""

class Calculator:

    """" The add method takes two int parameters. The add() method will them
return the sum of the two ints."""
    @staticmethod
    def add(a, b):
        return a + b

    """ The subtract method takes two int parameters. It will then return the
    difference of the two ints."""
    @staticmethod
    def subtract(a,b):
        return a - b

    """ The multiple method takes two int parameters. It will then return the 
    product of the two ints """
    @staticmethod
    def multiply(a,b):
        return a * b

    """ The division method takes two int parameters. It will then return the
    quotient of the two ints"""
    @staticmethod
    def divide(a,b):
        return a / b
