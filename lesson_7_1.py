class Matrix:
    def __init__(self, dict_of_dict):
        self.dict_of_dict = dict_of_dict

    def __str__(self):
        return '\n'.join(' '.join([str(i) for i in el]) for el in self.dict_of_dict)

    def __add__(self, other):
        if len(self.dict_of_dict) != len(other.dict_of_dict):
            return 'Сложение невозможно, матрицы не равны'
        for el_1, el_2 in zip(self.dict_of_dict, other.dict_of_dict):
            if len(el_1) != len(el_2):
                return 'Сложение невозможно, матрицы не равны'
        m3 = [[x + y for x, y in zip(el_1, el_2)] for el_1, el_2 in zip(self.dict_of_dict, other.dict_of_dict)]
        return Matrix(m3)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = Matrix([[1, 1, 1], [2, 2, 2]])
print(matrix_1)
print(matrix_1 + matrix_2)
