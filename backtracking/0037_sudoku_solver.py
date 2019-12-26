from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.boxes = defaultdict(set)
        
    def _is_valid(self, row, col, num):
        if num not in self.rows[row] and\
            num not in self.cols[col] and\
            num not in self.boxes[(row // 3, col // 3)]:
            return True
        else:
            return False
    
    def _assign(self, board, row, col, num):
        board[row][col] = num
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.boxes[(row // 3, col // 3)].add(num)
        
    def _remove(self, board, row, col):
        n = board[row][col]
        board[row][col] = '.'
        self.rows[row].discard(n)
        self.cols[col].discard(n)
        self.boxes[(row // 3, col // 3)].discard(n)
        
    def _backtrack(self, board, row, col) -> bool:
        if col < 9:
            if board[row][col] == '.':
                for n in range(1, 10):
                    if self._is_valid(row, col, str(n)):
                        self._assign(board, row, col, str(n))
                        if self._backtrack(board, row, col + 1):
                            return True

                        # backtrack
                        self._remove(board, row, col)
                
                return False
            else:
                return self._backtrack(board, row, col + 1)
        else:
            col = 0
            row += 1
            
            if row == 9:
                return True
            else:
                return self._backtrack(board, row, col)
                
    
    def solveSudoku(self, board: list) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.boxes[(i // 3, j // 3)].add(num)
                    
        self._backtrack(board, 0, 0)
        

if __name__ == "__main__":
    solu = Solution()
    m = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    solu.solveSudoku(m)

    print(m)