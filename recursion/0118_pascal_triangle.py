class Solution:
    def __init__(self):
        self.cache = {}

    def _pascal_recursive(self, row, col) -> int:
        if col == 0 or row == col:
            self.cache[(row, col)] = 1
            return 1
        else:
            upper = self.cache.get((row - 1, col), None)
            upper_left = self.cache.get((row - 1, col - 1), None)
            if upper and upper_left:
                # dynamic programming
                self.cache[(row, col)] = upper + upper_left
                return upper + upper_left
            else:
                # recursive
                self.cache[(row, col)] = self._pascal_recursive(row - 1, col) + self._pascal_recursive(row - 1, col - 1)
                return self.cache[(row, col)]


    def generate(self, numRows: int) -> list:
        res = [[0 for _ in range(i + 1)] for i in range(numRows)]

        for i in range(numRows):
            for j in range(i + 1):
                res[i][j] = self._pascal_recursive(i, j)

        return res

        