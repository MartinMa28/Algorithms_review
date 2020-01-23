class Solution:
    
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    @staticmethod
    def _on_board(board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
    
    def _backtrack(self, board, row, col, word):
        if not word:
            return True
        
        if self._on_board(board, row, col) and \
            board[row][col] == word[0]:
            board[row][col] = '$'
            for d in self.directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if self._backtrack(board, new_row, new_col, word[1:]):
                    return True
            
            # backtrack
            board[row][col] = word[0]
        
        return False
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._backtrack(board, i, j, word):
                    return True
                
        return False