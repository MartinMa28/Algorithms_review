class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if nums == []:
            return 0
        
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        
        return max(dp)