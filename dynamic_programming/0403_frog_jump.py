class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def _can_cross(self, stones, cur_idx, step, last_idx) -> bool:
        if (cur_idx, step) in self.memo:
            return self.memo[(cur_idx, step)]
        
        if cur_idx == last_idx:
            return True
        elif cur_idx > last_idx:
            return False
        else:
            if cur_idx not in stones:
                return False

            for s in (step - 1, step, step + 1):
                if s > 0:
                    if self._can_cross(stones, cur_idx + s, s, last_idx):
                        self.memo[(cur_idx, step)] = True
                        return True
                    
                self.memo[(cur_idx, step)] = False
            return False
            
    
    
    def canCross(self, stones: List[int]) -> bool:
        """
        Dynamic programming (3 choices in each step)
        1. current pos is reachable <- at least it's able to reach 
            a further reachable position
        2. overlaping
        """
        return self._can_cross(set(stones), 1, 1, stones[-1])