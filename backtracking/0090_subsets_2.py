class Solution:
    def __init__(self):
        self.res = []
        
        
    def _backtrack(self, nums, cur_set):
        self.res.append(cur_set[:])
            
        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                continue
            
            cur_set.append(n)
            self._backtrack(nums[idx + 1:], cur_set)
            
            # backtrack
            cur_set.pop()
            
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self._backtrack(nums, [])
        
        return self.res