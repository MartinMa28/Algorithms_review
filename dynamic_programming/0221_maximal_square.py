class Solution:
    def __init__(self):
        self.memo = {}
    
    def _on_board(self, row, col):
        return row >= 0 and row < self.m and col >= 0 and col < self.n
    
    def _dfs(self, row, col):
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        
        if self._on_board(row, col) and self.matrix[row][col] == '1':
            up = self._dfs(row - 1, col)
            left = self._dfs(row, col - 1)
            up_left = self._dfs(row - 1, col - 1)
            
            self.memo[(row, col)] = min((up, left, up_left)) + 1
            return min((up, left, up_left)) + 1
        else:
            self.memo[(row, col)] = 0
            return 0
            
    
    def maximalSquare(self, matrix: list) -> int:
        if matrix == []:
            return 0
        
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        
        largest = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == '1':
                    largest = max((largest, self._dfs(i, j)))
                    
        return largest ** 2