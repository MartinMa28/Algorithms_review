class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        last_x, last_y = coordinates[-1]
        first_x, first_y = coordinates[0]
        vertical = False
        slope = 0
        if last_x == first_x:
            vertical = True
        else:
            slope = (last_y - first_y) / (last_x - first_x)
        
        for i in range(1, len(coordinates) - 1):
            x, y = coordinates[i]
            if vertical:
                if x != first_x:
                    return False
            else:
                if x == first_x:
                    return False
                elif not (y - first_y) / (x - first_x) == slope:
                    return False
            
        return True