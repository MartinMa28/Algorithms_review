class Solution:
    def isValidSudoku(self, board: list) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in row_set[i] or num in col_set[j] or \
                        num in box_set[i // 3][j // 3]:
                        return False
                    else:
                        row_set[i].add(num)
                        col_set[j].add(num)
                        box_set[i // 3][j // 3].add(num)
                        
        return True