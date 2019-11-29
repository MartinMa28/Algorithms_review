class Solution:
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.found = False
        self.visited = set()
    
    def _on_board(self, row, col):
        return row >= 0 and row < len(self.board) \
                and col >= 0 and col < len(self.board[0])

    
    def _dfs(self, row, col, idx) -> bool:
        if self._on_board(row, col) and (row, col) not in self.visited:
            if self.board[row][col] == self.word[idx]:
                self.visited.add((row, col))
                if idx == len(self.word) - 1:
                    return True
                
                for d in self.directions:
                    new_row = d[0] + row
                    new_col = d[1] + col
                    
                    if self._dfs(new_row, new_col, idx + 1):
                        return True
                
                # backtracking
                self.visited.discard((row, col))
        
        return False
                        
    
    def exist(self, board: list, word: list) -> bool:
        if board == None or board == [] or board == [[]]:
            return False
        
        self.board = board
        self.word = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._dfs(i, j, 0):
                    return True
                
        return False
if __name__ == "__main__":
    solu = Solution()
    print(solu.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))