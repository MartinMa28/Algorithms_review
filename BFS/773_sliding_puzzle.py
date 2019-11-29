from collections import deque
from copy import deepcopy

class Solution:
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
    def _on_board(self, row, col):
        return row >= 0 and row < 2 and col >= 0 and col < 3
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    row = i
                    col = j
                    break
        
        visited = set()
        t_b = tuple([tuple(r) for r in board])
        visited.add(t_b)
        queue = deque([(row, col, board, 0)])
        
        while len(queue) > 0:
            row, col, board, move = queue.popleft()
            print(board)
            if board == [[1,2,3],[4,5,0]]:
                return move
            
            for d in self.directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if self._on_board(new_row, new_col):
                    
                    board[row][col], board[new_row][new_col] = \
                    board[new_row][new_col], board[row][col]
                    
                    t_n_b = tuple([tuple(r) for r in board])
                    
                    if t_n_b not in visited:
                        visited.add(t_n_b)
                        queue.append((new_row, new_col, deepcopy(board), move + 1))
                        
                    board[row][col], board[new_row][new_col] = \
                    board[new_row][new_col], board[row][col]
                        
        return -1