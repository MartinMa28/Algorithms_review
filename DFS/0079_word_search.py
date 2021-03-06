class Solution:
    
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    def _on_board(self, row, col):
        return row >= 0 and row < self.rows and col >= 0 and col < self.cols
    
    def _dfs(self, board, word, idx, row, col):
        if idx == len(word):
            return True
        else:
            if self._on_board(row, col) and board[row][col] == word[idx]:
                board[row][col] = '$'
                
                for d in self.directions:
                    new_row = row + d[0]
                    new_col = col + d[1]

                    if self._dfs(board, word, idx + 1, new_row, new_col):
                        return True
                
                board[row][col] = word[idx]
                return False
            else:
                return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._dfs(board, word, 0, i, j):
                    return True
        
        return False

if __name__ == "__main__":
    solu = Solution()
    print(solu.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))