class Car:
    def __init__(self, name, fuel_consumption, fuel_lvl, low_fuel, tank_limit, speed):
        self.name = name
        self.fuel_consumption = fuel_consumption
        self.fuel_lvl = fuel_lvl
        self.low_fuel = low_fuel
        self.tank_limit = tank_limit
        self.speed = speed
        self._odometer = 0

    @property
    def odometer(self):
        return self._odometer

    @property
    def fuel_indicator(self):
        if self.fuel_lvl < self.low_fuel:
            return True
        return False

    def drive(self, distance):
        fuel_normalization = self.fuel_consumption / 100
        max_distance = self.fuel_lvl / fuel_normalization
        if distance > max_distance:
            distance = max_distance
        fuel_needed = distance * fuel_normalization
        self.fuel_lvl = self.fuel_lvl - fuel_needed
        self._odometer += distance
        time_h = distance // self.speed
        time_min = round(((distance / self.speed) - (distance // self.speed)) * 60)
        print(f"Czas przejazdu {distance}km to {time_h} godzin i {time_min} minut.")
        return fuel_needed

    def tank(self, new_fuel):
        max_fuel = self.tank_limit - self.fuel_lvl
        if new_fuel + self.fuel_lvl > self.tank_limit:
            new_fuel = max_fuel
            print("Zatankowano już do pełna!")
        self.fuel_lvl += new_fuel
        return new_fuel
