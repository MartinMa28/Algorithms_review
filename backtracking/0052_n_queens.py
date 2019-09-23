class Solution:
    def __init__(self):
        self.queens = set()
        self.count = 0

    def _place_queen(self, row, col):
        self.queens.add((row, col))

    def _remove_queen(self, row, col):
        self.queens.discard((row, col))

    def _is_safe(self, row, col):
        # Iterates through self.queens to check if the queens
        # attack each other.
        for q in self.queens:
            if q[0] == row:
                return False
            if q[1] == col:
                return False
            if abs((q[0] - row) / (q[1] - col)) == 1:
                return False
        
        return True

    def _backtrack_n_queens(self, row: int, n: int) -> None:
        for col in range(n):
            if self._is_safe(row, col):
                self._place_queen(row, col)

                if row == n - 1:
                    # Put the final queen successfully.
                    self.count += 1
                else:
                    self._backtrack_n_queens(row + 1, n)

                # backtrack
                self._remove_queen(row, col)

    def totalNQueens(self, n: int) -> int:
        self._backtrack_n_queens(row=0, n=n)
        res = self.count
        self.count = 0

        return res