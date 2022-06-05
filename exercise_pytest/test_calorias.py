# test_calorias.py

import pytest
from exercise_pytest.calorias import *

# Realizar un test para comprobar que el número de calorias inicial es 0
def test_default_initial_amount():
    calory = Calorias()
    assert calory.quantity == 0


# Realizar un test que inicialice el número de calorias a 100 y compruebe que se ha añadido correctamente
def test_setting_initial_amount():
    calory = Calorias(100)
    assert calory.quantity == 100

# Realizar un test que inicialice el número de calorias a 10. Añada 90 calorias y finalmente que compruebe que se ha añadido correctamente
def test__add_calories():
    calory = Calorias(10)
    calory.add_calories(90)
    assert calory.quantity == 100

# Realizar un test que inicialice el número de calorias a 20. Que gaste 10 calorias y finalmente que compruebe que se han gastado correctamente
def test_spend_calories():
    calory = Calorias(20)
    calory.spend_calories(10)
    assert calory.quantity == 10

# Realizar un test que no de un error si queremos gastar mas calorias de las que realmente tenemos
def test_spend_calories_raises_exception_on_insufficient_amount():
    calory = Calorias()
    with pytest.raises(InsufficientAmount):
        calory.spend_calories(100)
