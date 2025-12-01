class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = []

    def place(self, row, col):
        self.queens.append((row, col))

    def remove(self, row, col):
        self.queens.remove((row, col))

    def is_safe(self, row, col):
        for qr, qc in self.queens:
            if qr == row or qc == col:
                return False
            if abs(qr - row) == abs(qc - col):
                return False
        return True

    def _solve_recursive(self, col=0, solutions=None):
        if solutions is None:
            solutions = []

        if col == self.n:
            solutions.append(list(self.queens))
            return solutions

        for row in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                self._solve_recursive(col + 1, solutions)
                self.remove(row, col)

        return solutions

    def solve(self):
        return self._solve_recursive()

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

if __name__ == "__main__":
    for n in [1, 2, 3, 4, 8]:
        solutions = solve(n)
        print(f"n = {n}, liczba rozwiązań = {len(solutions)}")
