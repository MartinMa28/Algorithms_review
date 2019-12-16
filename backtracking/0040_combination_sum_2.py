class Solution:
    def __init__(self):
        self.combs = set()
        
    def _backtrack(self, candidates, cur, target):
        if sum(cur) > target:
            return
        elif sum(cur) == target:
            self.combs.add(cur)
        else:
            for idx, num in enumerate(candidates):
                self._backtrack(candidates[idx + 1:], cur + (num, ), target)
    
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        self._backtrack(candidates, tuple(), target)
        
        return self.combs