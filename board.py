class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = []

    # dodanie krolowej na planszy
    def place(self, row, col):
        self.queens.append((row, col))

    # usuniecie krolowej z planszy
    def remove(self, row, col):
        self.queens.remove((row, col))

    # sprawdzenie ustawionych juz krolowych
    def is_safe(self, row, col):
        for qr, qc in self.queens:
            if qr == row or qc == col:
                return False
            if abs(qr - row) == abs(qc - col):
                return False
        return True

    # lista rozwiazan
    def _solve_recursive(self, col=0, solutions=None):
        if solutions is None:
            solutions = []
        # jesli ustawiono krolowa w kazdej kolumnie to mamy rozwiazanie
        if col == self.n:
            solutions.append(list(self.queens))
            return solutions

        # ustawiamy krolowa w kazdym wierszu danej kolumny
        for row in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                self._solve_recursive(col + 1, solutions)
                self.remove(row, col)

        return solutions

    def solve(self):
        return self._solve_recursive()

    # tekstowa reprezantacjsa planszy
    def __str__(self):
        rows = []
        for r in range(self.n):
            row_chars = []
            for c in range(self.n):
                if (r, c) in self.queens:
                    row_chars.append('Q')
                else:
                    row_chars.append('.')
            rows.append(' '.join(row_chars))
        return '\n'.join(rows)

    def __repr__(self):
        return f"Board(n={self.n}, queens={self.queens})"


def solve(n=8):
    board = Board(n)
    return board.solve()

# testy z roznymi n
if __name__ == "__main__":
    for n in [1, 2, 3, 4, 8]:
        solutions = solve(n)
        print(f"n = {n}, liczba rozwiązań = {len(solutions)}")
