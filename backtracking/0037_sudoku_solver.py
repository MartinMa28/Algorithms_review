class Solution:
    def _backtrack(self, board, row, col) -> bool:
        if col == 9:
            # At the last column
            if row == 8:
                # At the bottom right corner, found the result
                return True
            
            # Check the next line's first entry
            row += 1
            col = 0
            return self._backtrack(board, row, col)
        elif board[row][col] != '.':
            return self._backtrack(board, row, col + 1)
        else:
            for n in range(1, 10):
                n = str(n)
                board[row][col] = n
                if self._is_valid(board, row, col):
                    if self._backtrack(board, row, col + 1):
                        return True
                    
                # backtrack
                board[row][col] = '.'
            
            return False
            
    def _is_valid(self, board, row, col):
        # Check the row.
        unique = set()
        for num in board[row]:
            if num != '.':
                if num in unique:
                    return False
                else:
                    unique.add(num)
        
        # Check the column.
        unique.clear()
        for num in [row[col] for row in board]:
            if num != '.':
                if num in unique:
                    return False
                else:
                    unique.add(num)
                    
        top_left_row = (row // 3) * 3
        top_left_col = (col // 3) * 3
        
        # Check the 3x3 box.
        unique.clear()
        for i in range(3):
            for j in range(3):
                num = board[top_left_row + i][top_left_col + j]
                if num != '.':
                    if num in unique:
                        return False
                    else:
                        unique.add(num)
                        
        return True
    
    def solveSudoku(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._backtrack(board, 0, 0)


if __name__ == "__main__":
    solu = Solution()
    m = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    solu.solveSudoku(m)

    print(m)