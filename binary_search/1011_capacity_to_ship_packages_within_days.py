class Solution:
    
    @staticmethod
    def _days(weights, capacity):
        load = 0
        days = 0
        
        for w in weights:
            if load + w <= capacity:
                load += w
            else:
                load = w
                days += 1
                
        return days + 1
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_capa = max(weights)
        max_capa = sum(weights)
        
        while min_capa < max_capa:
            mid = (min_capa + max_capa) // 2
            
            if self._days(weights, mid) <= D:
                max_capa = mid
            else:
                min_capa = mid + 1
        
        return min_capa