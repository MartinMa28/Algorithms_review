class Solution:
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


    def _off_board(self, row, col):
        return (row < 0) or (row > len(self.board) - 1)\
                or (col < 0) or (col > len(self.board[0]) - 1)


    def _dfs(self, row, col):
        if self._off_board(row, col):
            return
        
        if self.board[row][col] == 'O':
            self.board[row][col] = 'V'
            for d in self.directions:
                new_row = row + d[0]
                new_col = col + d[1]

                self._dfs(new_row, new_col)

            
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        
        self.board = board
        h = len(self.board)
        w = len(self.board[0])
        # Start the DFS from Os that are on the boundary.
        for i in range(h):
            self._dfs(i, 0)
            self._dfs(i, w - 1)

        for j in range(w):
            self._dfs(0, j)
            self._dfs(h - 1, j)

        for i in range(h):
            for j in range(w):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'

                elif self.board[i][j] == 'V':
                    self.board[i][j] = 'O'