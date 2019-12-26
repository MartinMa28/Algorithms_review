from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.row_nums = defaultdict(set)
        self.col_nums = defaultdict(set)
        self.square_nums = defaultdict(set)
    
    def _validate(self, board, r_i, c_i, n) -> bool:
        if n in self.row_nums[r_i] or n in self.col_nums[c_i] or\
            n in self.square_nums[(r_i // 3, c_i // 3)]:
            return False
        
        board[r_i][c_i] = n
        self.row_nums[r_i].add(n)
        self.col_nums[c_i].add(n)
        self.square_nums[(r_i // 3, c_i // 3)].add(n)
        
        return True
    
    def _remove_num(self, board, row, col):
        n = board[row][col]
        board[row][col] = '.'
        
        self.row_nums[row].discard(n)
        self.col_nums[col].discard(n)
        self.square_nums[(row // 3, col // 3)].discard(n)
    
    def _backtrack(self, board, row, col):
        if col < 9:
            if board[row][col] == '.':
                for i in range(1, 10):
                    if self._validate(board, row, col, str(i)):
                        if self._backtrack(board, row, col + 1):
                            return True

                    self._remove_num(board, row, col)
                    

                return False
            else:
                return self._backtrack(board, row, col + 1)
        else:
            row += 1
            col = 0
            
            if row == 9:
                return True
            else:
                return self._backtrack(board, row, col)
    
    def solveSudoku(self, board: list) -> None:
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    self.row_nums[i].add(num)
                    self.col_nums[j].add(num)
                    self.square_nums[(i // 3, j // 3)].add(num)
        
        self._backtrack(board, 0, 0)
        


if __name__ == "__main__":
    solu = Solution()
    m = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    solu.solveSudoku(m)

    print(m)