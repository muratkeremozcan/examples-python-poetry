"""A module to implement the BasicCalculator.
"""
import numpy as np

class BasicCalculator:
    """A class for arithmetic operations on numbers    
    """
    def add(self, x, y):
        return np.add(x, y)

    def subtract(self, x, y):
        return np.subtract(x, y)

    def multiply(self, x, y):
        return np.multiply(x, y)

    def divide(self, x, y):
        return np.divide(x, y)

    def power(self, x, y):
        return np.power(x, y)