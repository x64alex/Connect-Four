from domain.table import Table


class Repository:
    def __init__(self, m, n):
        self.table = Table(m, n)
        self._table = self.table.table
        self.number_columns = m
        self.number_rows = n

    def move(self, a, b, val):
        self.table.set(a, b, val)

    def check_win(self):
        return self.check_win_row() or self.check_win_column() or self.check_win_diagonal()

    def check_draw(self):
        for i in range(0, self.table.number_rows()):
            for j in range(0, self.table.number_columns()):
                if self._table[i][j] == 0:
                    return False
        return True

    def check_win_row(self):
        for i in range(0, self.table.number_rows()):
            for j in range(0, self.table.number_columns() - 3):
                if self._table[i][j] == self._table[i][j + 1] == self._table[i][j + 2] == self._table[i][j + 3] and \
                        self._table[i][j] != 0:
                    return True
        return False

    def check_win_column(self):
        for i in range(0, self.table.number_rows() - 3):
            for j in range(0, self.table.number_columns()):
                if self._table[i][j] == self._table[i + 1][j] == self._table[i + 2][j] == self._table[i + 3][j] and \
                        self._table[i][j] != 0:
                    return True
        return False

    def check_win_diagonal(self):
        for i in range(0, self.table.number_rows() - 3):
            for j in range(0, self.table.number_columns() - 3):
                if self._table[i][j] == self._table[i + 1][j + 1] == self._table[i + 2][j + 2] == self._table[i + 3][
                    j + 3] and \
                        self._table[i][j] != 0:
                    return True

                if self._table[i + 3][j] == self._table[i + 2][j + 1] == self._table[i + 1][j + 2] == self._table[i][
                    j + 3] and \
                        self._table[i + 3][j] != 0:
                    return True
        return False

    def validate_move(self, a, b):
        if self._table[a][b] != 0:
            return False
        for i in range(a + 1, self.table.number_rows()):
            if self._table[i][b] == 0:
                return False
        return True

    def possible_moves(self):
        moves = []
        for i in range(0, self.table.number_rows()):
            for j in range(0, self.table.number_columns()):
                if self.validate_move(i, j):
                    moves.append([i, j])

        return moves
