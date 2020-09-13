class Race:
    def __init__(self, cars, track, laps):
        self.laps = laps

    def start(self):
        for car in cars:  # tankowanie do pełna aut
            car.add_fuel(car.tank_capacity)
        end_rank = []  # deklarowanie listy z koncowym rankingiem
        ranking = {f"{car.name}": {"RidDist": 0, "Lap": 0} for car in
                   cars}  # lista [a,b] a-miejsce, b- przejechany dystans
        whole_dist = self.laps * track.track_length  # pelna dlugosc wyscigu
        min_speed = min([car.speed for car in
                         cars])  # predkosc minimalna do wyznaczenia teoretycznego czasu ukonczenia wyscigu przez najwolniejsze auto
        max_time = whole_dist / min_speed  # maksymalny czas rajdu
        time_div = 20  # dzielnik czasu pokonania jednego okrazenia przez najwolniejsze auto
        time_step = (max_time / self.laps) / time_div  # krok czasowy rajdu
        print(f"min_speed: {min_speed}")
        print(f"max_time: {max_time}")
        print(f"time_step: {time_step}")
        t = 0  # zmienna okreslajaza chwile czasowa rajdu
        while t <= max_time + time_step:
            ridden_lap_ind = False  # wskaznik czy w kroku czasowym dowolne auto przekroczylo okrazenie
            for car in cars:  # aktualizacja stanow aut w chwili czasowej t
                if ranking[car.name]["Lap"] == self.laps:  # jesli auto ukonczylo wyscig to nastepne
                    continue
                teor_dist = time_step * car.speed  # teoretyczny dystans przejechany przez auto w czasie time_step
                car.drive(teor_dist)  # przejechanie teoretycznego dystansu w kroku czasowy
                ranking[car.name][
                    "RidDist"] = car.odometer  # dopisanie rzeczywistego przejechanego dystansu przez auto do slownika
                if ranking[car.name][
                    "Lap"] < car.odometer // track.track_length:  # obliczenie czy auto zrobilo nowe pelne okrazenie
                    ranking[car.name]["Lap"] += 1  # i aktualizacja aktualnego okrazenia w slowniku
                    print(f'### LAP {ranking[car.name]["Lap"]} dla auta {car.name}')
                    ridden_lap_ind = True  # wskaznik drukujacy pozniej aktualny ranking (ze wzgledu ze dowolne auto dokonalo okrazenia)
                    if ranking[car.name][
                        "Lap"] == self.laps:  # jesli auto ukonczylo wyscik do dopisanie nazwy auta do listy koncowej wycigu
                        end_rank.append(car.name)
                        break
            if ridden_lap_ind:
                tmp_rank = sorted(ranking.items(), key=lambda x: x[1]["RidDist"],
                                  reverse=True)  # krotka posortowana po przejechanek odleglosci
                tmp_rank = [i[0] for i in tmp_rank]  # wyodrebnienie tylko nazw aut z posortowanej krotki
                print(f"### {tmp_rank} ###")
                lack_fuel = [car.name for car in cars if car.fuel_tank == 0.0]  # lista z autami ktorym zabraklo benzyny
                print(f"Brak benzyny w {lack_fuel}")
            t += time_step  # krok czasowy
        print(f"Wyscig ukonczyli: {end_rank}")
