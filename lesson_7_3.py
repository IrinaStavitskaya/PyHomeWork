class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num <= 0:
            return 'Разница числа клеток меньше или равна 0'
        else:
            return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return int(self.num / other.num)

    def make_order(self):
        cell_order = ''
        for i in range(1, self.num + 1):
            if i % 5 == 0:
                cell_order += '*\n'
            else:
                cell_order += '*'
        return cell_order


cell_1 = Cell(2)
cell_2 = Cell(5)
cell_3 = Cell(17)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2 / cell_1)
print(cell_3.make_order())
