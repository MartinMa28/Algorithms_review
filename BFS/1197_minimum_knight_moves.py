from collections import deque

class Solution:
    def __init__(self):
        self.directions = (
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
            (2, 1),
            (-2, 1),
            (2, -1),
            (-2, -1)
        )
    
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            popped_x, popped_y, steps = queue.popleft()
            if popped_x == x and popped_y == y:
                return steps
            
            delta_x = x - popped_x
            delta_y = y - popped_y
            
            for d in self.directions:
                if (abs(delta_x) <= 1 and abs(delta_y) <= 1) or\
                    (delta_x * d[0] >= 0 and delta_y * d[1] >= 0):
                    new_x = popped_x + d[0]
                    new_y = popped_y + d[1]

                    if (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y, steps + 1))