from collections import deque

class Solution:
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
    def _off_board(self, row, col, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        return row < 0 or row >= m or col < 0 or col >= n 
    
    def _bfs(self, matrix, queue):
        visited = set()
        
        while len(queue) > 0:
            r, c, dist = queue.popleft()
            if dist < matrix[r][c]:
                matrix[r][c] = dist
                
            visited.add((r, c))
            for d in self.directions:
                new_r = r + d[0]
                new_c = c + d[1]
                
                if not self._off_board(new_r, new_c, matrix) and (new_r, new_c) not in visited:
                    if matrix[new_r][new_c] > 0:
                        queue.append((new_r, new_c, dist + 1))
                        
            
    
    def wallsAndGates(self, rooms: list) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Do BFS from all of zeros in the matrix
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
                    
        self._bfs(rooms, queue)
                    
        