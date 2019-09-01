from copy import deepcopy

class Solution:
    def _is_safe(self, row, col) -> bool:
        # check this row on the left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # check the upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # check the lower diagonal on the left side
        for i, j in zip(range(row, self.size), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        return True
                

    def _recursive_util(self, col) -> bool:
        if col == self.size:
            self.results.append(deepcopy(self.board))
            return True
        
        res = False
        for row in range(self.size):
            if self._is_safe(row, col):     
                # In current column, found a row to insert.
                self.board[row][col] = 1
                res = self._recursive_util(col + 1) or res
                # backtracking
                self.board[row][col] = 0
                # if self._recursive_util(col + 1):
                #     return True
                # else:
                #     # backtracking
                #     self.board[row][col] = 0

        return res


    def solveNQueens(self, n: int) -> list:
        self.size = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.results = []

        self._recursive_util(0)
        return self._str_transfer()


    def _str_transfer(self) -> list:
        str_results = []
        for res in self.results:
            r = []
            for row in res:
                s = ''
                for num in row:
                    s += '.' if num == 0 else 'Q'
                r.append(s)
            str_results.append(r)
        
        return str_results


if __name__ == "__main__":
    solu = Solution()
    print(solu.solveNQueens(4))