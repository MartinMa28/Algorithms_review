class Solution:
    def __init__(self):
        self.res = []
        
    def _backtrack(self, nums, cur_perm):
        if nums == []:
            self.res.append(cur_perm[:])
            
        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                continue
            
            cur_perm.append(n)
            self._backtrack(nums[:idx] + nums[idx + 1:], cur_perm)
            
            # backtrack
            cur_perm.pop()
    
    def permuteUnique(self, nums: list) -> list:
        nums.sort()
        self._backtrack(nums, [])
        
        return self.res