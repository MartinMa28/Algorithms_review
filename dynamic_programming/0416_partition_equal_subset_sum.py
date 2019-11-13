class Solution:
    def __init__(self):
        self.memo = {}
    
    def _subset_recursive(self, nums, target, cur):
        if (cur, target) in self.memo:
            return self.memo[(cur, target)]
        
        if target == 0:
            # Found a subset that sums up to the target.
            self.memo[(cur, target)] = True
            return self.memo[(cur, target)]
        
        if target < 0 or cur == len(nums):
            # The target doesn't decrease to zero.
            self.memo[(cur, target)] = False
            return self.memo[(cur, target)]
        
        self.memo[(cur, target)] = self._subset_recursive(nums, target, cur + 1) or \
                                self._subset_recursive(nums, target - nums[cur], cur + 1)
        return self.memo[(cur, target)]
    
    def canPartition_top_down(self, nums: list) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 > 0:
            return False
        
        target = total_sum >> 1
        
        return self._subset_recursive(nums, target, 0)

    def canPartition(self, nums: list) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 > 0:
            return False
        
        target = total_sum >> 1
        
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        
        for i in range(len(nums) + 1):
            dp[i][0] = True
            
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                n = nums[i - 1]
                if j - n >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - n]
                else:
                    dp[i][j] = dp[i - 1][j]
                
        return dp[-1][-1]