class Track:
    def __init__(self, name, lap_length, laps):
        """
            Class Track initialization
        """
        self.name = name
        self.lap_length = lap_length
        self.laps = laps

    @property
    def total_length(self):
        return self.lap_length * self.laps
