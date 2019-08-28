class Soluton:
    def numIslands(self, grid: list) -> int:
        if grid == None or grid == [] or grid == [[]]:
            return 0
        
        stack = []
        count = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    stack.append((i, j))
                
                while len(stack) > 0:
                    vtx_coor = stack.pop()
                    grid[vtx_coor[0]][vtx_coor[1]] = '#'

                    for d in directions:
                        next_row = vtx_coor[0] + d[0]
                        next_col = vtx_coor[1] + d[1]

                        if next_row < len(grid) \
                            and next_row >= 0 \
                            and next_col < len(grid[0]) \
                            and next_col >= 0 \
                            and grid[next_row][next_col] == '1':
                            stack.append((next_row, next_col))

        return count

    
    def numIslands_recursive(self, grid: list) -> int:
        if grid == None or grid == [] or grid == [[]]:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self._dfs(grid, i, j)
                
        return count

    def _dfs(self, grid, row, col) -> None:
        grid[row][col] = '#'
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for d in directions:
            next_row = row + d[0]
            next_col = col + d[1]
            if next_row >= 0 \
                and next_row < len(grid) \
                and next_col >= 0 \
                and next_col < len(grid[0]) \
                and grid[next_row][next_col] == '1':
                self._dfs(grid, next_row, next_col)

if __name__ == "__main__":
    solu = Soluton()
    print(solu.numIslands_recursive([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))