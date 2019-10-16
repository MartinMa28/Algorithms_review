class Solution:
    def __init__(self):
        self.results = []
    
    def _is_safe(self, row, col) -> bool:
        if sum(self.board[row]) > 0:
            return False
        
        if sum([r[col] for r in self.board]) > 0:
            return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i,j in zip(range(row, len(self.board)), range(col, len(self.board))):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, len(self.board)), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i,j in zip(range(row, -1, -1), range(col, len(self.board))):
            if self.board[i][j] == 1:
                return False

        return True

    
    def _place_queen(self, row, col):
        self.board[row][col] = 1

    
    def _remove_queen(self, row, col):
        self.board[row][col] = 0

    def _backtracking(self, row):
        if row == len(self.board):
            self.results.append(self._str_transfer())
            return

        for col in range(len(self.board[0])):
            if self._is_safe(row, col):
                self._place_queen(row, col)
                self._backtracking(row + 1)
                self._remove_queen(row, col)


    def _str_transfer(self) -> list:
        ret = []
        for row in self.board:
            s = ''
            for n in row:
                if n == 0:
                    s += '.'
                else:
                    s += 'Q'
            
            ret.append(s)

        return ret

    def solveNQueens(self, n: int) -> list:
        self.board = [[0 for _ in range(n)] for _ in range(n)]

        self._backtracking(0)

        return self.results
        

if __name__ == "__main__":
    solu = Solution()
    print(solu.solveNQueens(8))
    print(solu.results)