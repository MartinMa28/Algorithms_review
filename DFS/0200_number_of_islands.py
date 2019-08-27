class Soluton:
    def numIslands(self, grid: list) -> int:
        if grid == None or grid == [] or grid == [[]]:
            return 0
        
        stack = []
        visited = []
        count = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        stack.append((0, 0))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1
                
                while len(stack) > 0:
                    vtx_coor = stack.pop()
                    visited.append(vtx_coor)

                    for d in directions:
                        next_row = vtx_coor[0] + d[0]
                        next_col = vtx_coor[1] + d[1]

                        if grid[next_row][next_col] == 1 and (next_row, next_col) not in visited:
                            stack.append((next_row, next_col))

        return count


if __name__ == "__main__":
    solu = Soluton()
    print(solu.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))