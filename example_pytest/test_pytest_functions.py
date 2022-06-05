from example_pytest.pytest_functions import *


def test_square_func():
    n = 2
    assert square_func(n) == 1


def test_cube():
    n = 3
    assert cube(n) == 27


def test_calcula_media():
    assert calcula_media([5, 3, 1]) == 3


def test_capital_letter():
    assert capital_letter("sandro") == "Sandro"

"""
Para ejecutar los test me tendré que poner dentro del directorio y llamar a la función example_pytest
"""