from collections import defaultdict

class Solution:
    def __init__(self):
        self.row_set = defaultdict(set)
        self.col_set = defaultdict(set)
        self.box_set = defaultdict(set)
    
    def _is_valid(self, board, row, col, num) -> bool:
        if num in self.row_set[row]:
            return False
        
        if num in self.col_set[col]:
            return False
        
        if num in self.box_set[(row // 3, col // 3)]:
            return False
        
        return True
    
    
    def _add_num(self, board, row, col, num):
        board[row][col] = str(num)
        self.row_set[row].add(num)
        self.col_set[col].add(num)
        self.box_set[(row // 3, col // 3)].add(num)
        
    def _remove_num(self, board, row, col):
        num = board[row][col]
        board[row][col] = '.'
        self.row_set[row].discard(num)
        self.col_set[col].discard(num)
        self.box_set[(row // 3, col // 3)].discard(num)
    
    def _backtrack(self, board, row, col) -> bool:
        if col < 9:
            if board[row][col] != '.':
                return self._backtrack(board, row, col + 1)
            else:
                for i in range(1, 10):
                    if self._is_valid(board, row, col, str(i)):
                        self._add_num(board, row, col, str(i))
                        if self._backtrack(board, row, col + 1):
                            return True
                    
                        # backtrack
                        self._remove_num(board, row, col)
                
                return False
        else:
            row += 1
            col = 0
            
            if row == 9:
                return True
            else:
                return self._backtrack(board, row, col)
    
                
    def solveSudoku(self, board: list) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    self.row_set[i].add(num)
                    self.col_set[j].add(num)
                    self.box_set[(i // 3, j // 3)].add(num)
                    
        self._backtrack(board, 0, 0)
        
        

if __name__ == "__main__":
    solu = Solution()
    m = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    solu.solveSudoku(m)

    print(m)