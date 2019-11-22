class Solution:
    def __init__(self):
        self.res = []
    
    
    def _backtrack(self, candidate, target, cur_com):
        if sum(cur_com) > target:
            return
        elif sum(cur_com) == target:
            self.res.append(cur_com[:])
        else:
            for idx, n in enumerate(candidate):
                cur_com.append(n)
                self._backtrack(candidate[idx:], target, cur_com)
                
                # backtracking
                cur_com.pop()
    
    def combinationSum(self, candidate: list, target: int) -> list:
        self._backtrack(candidate, target, [])    
        
        return self.res