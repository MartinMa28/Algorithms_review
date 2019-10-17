class Soluton:
    def _off_board(self, row, col, board):
        return (row < 0) or (row > len(board) - 1) \
                or (col < 0) or (col > len(board[0]) - 1)
    
    
    def _dfs(self, row, col, board):
        if self._off_board(row, col, board):
            return
        
        if board[row][col] == '1':
            board[row][col] = '0'
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]

                self._dfs(new_row, new_col, board)
    
    
    def numIslands(self, grid: list) -> int:
        if grid == []:
            return 0
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    self._dfs(i, j, grid)
                
        return cnt

if __name__ == "__main__":
    solu = Soluton()
    print(solu.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))