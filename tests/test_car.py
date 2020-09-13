import pytest
import random

from wyscig_sda.car import Car


@pytest.fixture(params=[
    (
        8.3,
        random.randint(50, 100),
        random.randint(50, 100),
        random.randint(50, 100),
        random.randint(50, 100))
    for _ in range(10)
])
def random_cars(request):
    fuel_consumption, fuel_lvl, low_fuel, tank_limit, speed = request.param

    return Car(
        "test",
        fuel_consumption,
        fuel_lvl,
        low_fuel,
        tank_limit,
        speed
    )


@pytest.fixture()
def standard_car():
    return Car("standard", 6.1, 30, 10, 60, 100)


class TestOdometer:
    def test_odometer_new_car(self, random_cars):
        assert random_cars.odometer == 0

    def test_odometer_read_only(self, random_cars):
        with pytest.raises(AttributeError):
            random_cars.odometer = 100
