class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass_1m_1sm = 25

    def mass_asphalt(self, thickness):
        self.thickness = thickness
        return f'Масса асфальта для дороги: {(self._length * self._width * self.mass_1m_1sm * self.thickness) / 1000} т'


a = Road(5000, 20)
print(a.mass_asphalt(5))
