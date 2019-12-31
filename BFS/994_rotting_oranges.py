from collections import deque

class Solution:
    
    @staticmethod
    def _on_board(grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
    
    def orangesRotting(self, grid: list) -> int:
        queue = deque()
        oranges = 0
        rotten = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    oranges += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        while queue:
            popped = queue.popleft()
            rotten.append(popped[2])
            
            
            for d in directions:
                new_row = popped[0] + d[0]
                new_col = popped[1] + d[1]
                
                if self._on_board(grid, new_row, new_col) and \
                    grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, popped[2] + 1))
        
        
        if len(rotten) < oranges:
            return -1
        else:
            if rotten:
                return rotten[-1]
            else:
                return 0