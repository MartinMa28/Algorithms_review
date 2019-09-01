class Solution:
    def __init__(self, m):
        self.maze = m
        self.directions = ((1, 0), (0, 1))
        self.solution = [[0 for _ in range(len(self.maze[0]))] for _ in range(len(self.maze))]


    def _is_safe(self, row, col):
        if row >= 0 and \
            row < len(self.maze) and \
            col >= 0 and \
            col < len(self.maze[0]) and \
            self.maze[row][col] == 1:
            return True
        else:
            return False


    def _print_solution(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                print(self.solution[i][j], end=' ')
            print()

    
    def _recursive_util(self, row, col) -> bool:
        if row == len(self.maze) - 1 and col == len(self.maze[0]) - 1:
            # arrive the exit
            return True
        
        for d in self.directions:
            next_row = row + d[0]
            next_col = col + d[1]
            
            if self._is_safe(next_row, next_col):
                self.solution[next_row][next_col] = 1
                if self._recursive_util(next_row, next_col): 
                    return True
                else:
                    # backtracking
                    self.solution[next_row][next_col] = 0
        
        return False



    def solve_maze(self):
        self.solution[0][0] = 1
        if self._recursive_util(0, 0):
            self._print_solution()
        else:
            print('Solution does not exist!')


if __name__ == "__main__":
    maze = [[1, 0, 0, 0], 
            [1, 1, 1, 1], 
            [0, 1, 0, 0], 
            [1, 1, 1, 1]]

    solu = Solution(maze)
    solu.solve_maze()