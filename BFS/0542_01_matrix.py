class Solution:
    def updateMatrix(self, matrix: list) -> list:
        if matrix == None or matrix == [[]]:
            return [[]]
        
        queue = []
        rows = len(matrix)
        cols = len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        dist_m = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue
                else:
                    # starts BFS for the first 0 neighbor and count the distance
                    dist = 0
                    queue.append((i, j))
                    while len(queue) > 0:
                        coor = queue.pop(0)
                        dist += 1

                        for d in directions:
                            next_row = coor[0] + d[0]
                            next_col = coor[1] + d[1]
                            if next_row >= 0 \
                                and next_row < rows \
                                and next_col >= 0 \
                                and next_col < cols \
                                and matrix[next_row][next_col] != 0:
                                queue.append((next_row, next_col))
                            else:
                                break
                    
                    dist_m[i][j] = dist
        
        return dist_m

if __name__ == "__main__":
    solu = Solution()
    print(solu.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))