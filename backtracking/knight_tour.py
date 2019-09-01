class Solution():
    def __init__(self, n):
        self.size = n
        self.board = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        self.directions = ((2, 1), (-2, 1), (2, -1), (-2, -1), 
                            (1, 2), (-1, 2), (1, -2), (-1, -2))
    

    def _is_safe(self, row, col):
        if row >= 0 and \
            row < self.size and \
            col >= 0 and \
            col < self.size and \
            self.board[row][col] == -1:
            return True
        else:
            return False

    
    def _print_solution(self):
        for i in range(self.size):
            for j in range(self.size):
                print(str(self.board[i][j]).zfill(2), end=' ')
            print()
    

    def solve_knight_tour(self) -> None:
        # start from (0, 0)
        self.board[0][0] = 0

        # step counter for knight's position
        pos = 1
        if not self._recursive_util(0, 0, self.directions, pos):
            print('Solution does not exist!')
        else:
            self._print_solution()


    def _recursive_util(self, row, col, directions, pos) -> bool:
        if pos == self.size ** 2:
            return True
        
        for row_offset, col_offset in directions:
            next_row = row + row_offset
            next_col = col + col_offset    
            if self._is_safe(next_row, next_col):
                self.board[next_row][next_col] = pos
                if self._recursive_util(next_row, next_col, directions, pos + 1):
                    return True
                else:
                    # backtracking
                    self.board[next_row][next_col] = -1
        
        return False


if __name__ == '__main__':
    solu = Solution(5)
    solu.solve_knight_tour()