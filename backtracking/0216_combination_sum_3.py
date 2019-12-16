class Solution:
    def __init__(self):
        self.combs = []
        
    def _backtrack(self, candidates, cur, target, k):
        if len(cur) == k and sum(cur) == target:
            self.combs.append(cur[:])
            return
        
        if sum(cur) > target:
            return
        elif len(cur) < k:
            for idx, candi in enumerate(candidates):
                cur.append(candi)
                self._backtrack(candidates[idx + 1:], cur, target, k)
                
                # backtracking
                cur.pop()
    
    def combinationSum3(self, k: int, n: int) -> list:
        self._backtrack(range(1, 10), [], n, k)
        
        return self.combs