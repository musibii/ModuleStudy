# -*- coding: utf-8 -*-
# __file__  : test_Car.py
# __time__  : 2020/7/9 3:08 PM

from Car import Car
import pytest

speed_data = {45, 50, 55, 100}


# @pytest.fixture
# def my_car():
#     return Car(50)

# def test_cat_brake():
#     my_car.accelerate()
#
#     assert my_car.speed == 45


# def test_car_accelerate(my_car):
#     my_car.accelerate()
#     assert my_car.speed == 55


# def test_car_brake(my_car):
#     my_car.brake()
#     assert my_car.speed == 45

@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


@pytest.mark.parametrize("speed_accelerate", speed_data)
def test_car_accelerate(speed_accelerate):
    car = Car(50)
    car.accelerate()
    assert car.speed == speed_accelerate
