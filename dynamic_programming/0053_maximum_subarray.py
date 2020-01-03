class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Each slot means the sum of the max-subarray that ends at this index
        dp = [float('-inf')] * len(nums)
        
        """
        dp[i] = max((nums[i], dp[i - 1] + nums[i]))
        """
        
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max((nums[i], dp[i - 1] + nums[i]))
            
        return max(dp)