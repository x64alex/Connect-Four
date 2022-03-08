import copy


def construct_matrix(a, b, val):
    row = [val] * b
    matrix = []
    for i in range(0, a):
        matrix.append(copy.deepcopy(row))
    return matrix


class Table:
    def __init__(self, number_rows, number_columns):
        self.table = construct_matrix(number_rows, number_columns, 0)
        self.__rows = number_rows
        self.__columns = number_columns

    def value(self, a, b):
        return self.table[a][b]

    def set(self, a, b, value):
        self.table[a][b] = value

    def number_rows(self):
        return self.__rows

    def number_columns(self):
        return self.__columns

    def __str__(self):
        table = ''
        for row in self.table:
            for el in row:
                table = table + str(el) + ' '
            table = table + '\n'
        return table
