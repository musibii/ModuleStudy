from pytest_bdd import scenario, given, when, then
import pytest
from Car import Car

@pytest.fixture
def my_car():
    return Car()


@scenario('car.feature', 'Valid speed')
def test_speed_valid():
    pass


@scenario('car.feature', 'Invalid speed')
def test_speed_invalid():
    pass


@given("Speed is less than 160")
def set_valid_speed(my_car):
    my_car.speed = 50


@given("Speed is more than 160")
def set_invalid_speed(my_car):
    my_car.speed = 100


@when("Accelerated")
def car_accelerate(my_car):
    my_car.accelerate()


@then("Speed is valid")
def success(my_car):
    assert my_car.speed_validate()


@then("Speed is invalid")
def fail(my_car):
    assert not my_car.speed_validate()

