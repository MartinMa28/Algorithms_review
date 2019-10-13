from collections import deque

class Solution:
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.memo = {}
        
        
    def _is_safe(self, row, col, height, width):
        return row >= 0 and row < height and col >= 0 and col < width
    
    def _bfs(self, matrix, row, col) -> int:
        if matrix[row][col] == 0:
            self.memo[(row, col)] = 0
            return 0
        else:
            queue = deque()
            
            queue.append((row, col, 0))
            
            while len(queue) > 0:
                p_r, p_c, l = queue.popleft()
                if matrix[p_r][p_c] == 0:
                    self.memo[(p_r, p_c)] = l
                    return l
                else:
                    for d in self.directions:
                        if self._is_safe(p_r + d[0], p_c + d[1], len(matrix), len(matrix[0])):
                            if (p_r + d[0], p_c + d[1]) not in self.memo:
                                queue.append((p_r + d[0], p_c + d[1], l + 1))
                            else:
                                self.memo[(p_r, p_c)] = self.memo[(p_r + d[0], p_c + d[1])] + 1
                                return self.memo[(p_r, p_c)]
            
            
    
    def updateMatrix(self, matrix: list) -> list:
        dist = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dist[i][j] = self._bfs(matrix, i, j)
                
        return dist

if __name__ == "__main__":
    solu = Solution()
    print(solu.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))