# -*- coding: utf-8 -*-
"""calc
   Implements the Calculator
"""
from typing import Union


class Calculator:
    """
    Calculator
    """

    @staticmethod
    def addition(value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
        """
        Sum one value by another
        """
        return value1 + value2

    @staticmethod
    def subtraction(value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
        """
        Subtract one value by another
        """
        return value1 - value2

    @staticmethod
    def division(value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
        """
        Divides one value by another
        """
        try:
            result = value1 / value2
        except ZeroDivisionError as ex:
            return ex
        return result

    @staticmethod
    def multiplication(value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
        """
        Multiplies one value by another
        """
        return value1 * value2


calc = Calculator()
print(calc.multiplication(1, 2))
print(calc.subtraction(3, 2))
print(calc.division(4, 5))
print(calc.division(1, 0))
print(calc.addition(3, 2))
