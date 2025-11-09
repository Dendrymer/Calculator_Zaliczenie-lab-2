import pytest
from Calculator import Calculator
#test funkcji obliczeniowych kalkulatora:
def test_sum():
    calc = Calculator(10, 5)
    assert calc.sum() == 15

def test_sub():
    calc = Calculator(10, 5)
    assert calc.sub() == 5

def test_mul():
    calc = Calculator(10, 5)
    assert calc.mul() == 50

def test_div():
    calc = Calculator(10, 5)
    assert calc.div() == 2

#test dzielenei przez zero:
def test_div_by_zero():
    calc = Calculator(7, 0)
    assert calc.div() == "Błąd: nie można dzielić przez zero"

#test błędnych typów danych:
def test_invalid_type_str():
    with pytest.raises(TypeError):
        Calculator("abc", 2)

def test_invalid_type_none():
    with pytest.raises(TypeError):
        Calculator(3, None)

#test dostępu do atrybutów:
def test_op1_property():
    calc = Calculator(10, 5)
    assert calc.op1 == 10.0

def test_op2_property():
    calc = Calculator(10, 5)
    assert calc.op2 == 5.0
