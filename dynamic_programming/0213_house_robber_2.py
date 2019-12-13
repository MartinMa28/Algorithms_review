class Solution:
    def __init__(self):
        self.memo = {}
    
    def _rob(self, nums):
        if nums in self.memo:
            return self.memo[nums]
        
        if nums == ():
            return 0
        
        rob_this = nums[0] + self._rob(nums[2:])
        not_rob_this = self._rob(nums[1:])
        self.memo[nums] = max((rob_this, not_rob_this))
        
        return self.memo[nums]
        
    
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        rob_first = nums[0] + self._rob(tuple(nums[2:-1]))
        not_rob_first = self._rob(tuple(nums[1:]))
        
        return max((rob_first, not_rob_first))