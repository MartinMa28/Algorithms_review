class Solution:
    def __init__(self):
        self.res = []
    
    def _backtrack(self, nums, cur_set):
        self.res.append(cur_set.copy())
        
        for idx, n in enumerate(nums):
            cur_set.append(n)
            self._backtrack(nums[idx + 1:], cur_set)
            
            # backtrack
            cur_set.pop()
        
            
    
    def subsets(self, nums: list) -> list:
        self._backtrack(nums, [])

        return self.res