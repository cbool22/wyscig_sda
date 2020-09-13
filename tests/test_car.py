import pytest

from wyscig_sda.car import Car


@pytest.fixture()
def dummy_car():
    return Car("test", 6.1, 40, 10, 60, 90.0)


class TestOdometer:
    def test_odometer_new_car(self, dummy_car):
        assert dummy_car.odometer == 0

    def test_odometer_read_only(self, dummy_car):
        with pytest.raises(AttributeError):
            dummy_car.odometer = 100
