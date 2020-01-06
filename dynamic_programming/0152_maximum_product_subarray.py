class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [2, 3, -2, 4]
        
        max_dp: each slot means the maximum product of sub-array ends at that index
        min_dp: each slot means the minimum product of sub-array ends at that index
        
        max_dp[i] = max((max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i]))
        min_dp[i] = min((min_dp[i - 1] * nums[i], max_dp[i - 1] * nums[i], nums[i]))
        
        
        max(max_dp)
        """
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        max_prod = nums[0]
        
        for i in range(1, len(nums)):
            max_copy = max_dp[i - 1]
            max_dp[i] = max((max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i]))
            min_dp[i] = min((min_dp[i - 1] * nums[i], max_copy * nums[i], nums[i]))
            
            max_prod = max((max_prod, max_dp[i]))
            
        return max_prod