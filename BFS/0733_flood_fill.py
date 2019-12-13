from collections import deque

class Solution:
    
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
    def _on_image(self, row, col, image):
        return row >= 0 and row < len(image) and col >= 0 and col < len(image[0])

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image == None or image == [] or image == [[]]:
            return image
        
        queue = deque([(sr, sc)])
        src_color = image[sr][sc]
        visited = set([(sr, sc)])
        
        while len(queue) > 0:
            row, col = queue.popleft()
            image[row][col] = newColor
            
            for d in self.directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if self._on_image(new_row, new_col, image) and\
                    image[new_row][new_col] == src_color and\
                    (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        
        return image