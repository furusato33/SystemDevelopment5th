import pytest
from calculator.calculator import Calculator, InvalidInputException

def test_add_performance(benchmark):
    calc = Calculator()
    benchmark(calc.add, 100, -200)

def test_subtract_performance(benchmark):
    calc = Calculator()
    benchmark(calc.subtract, 100, -200)

def test_multiply_performance(benchmark):
    calc = Calculator()
    benchmark(calc.multiply, 100, -200)
    
def test_divide_performance(benchmark):
    calc = Calculator()
    benchmark(calc.divide, 100, -200)