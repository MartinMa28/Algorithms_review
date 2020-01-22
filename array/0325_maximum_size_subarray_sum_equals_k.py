class Solution:
    def maxSubArrayLen(self, nums: list, k: int) -> int:
        '''
        1 -1 5 -2 3             3
        '''
        if not nums:
            return 0
        
        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i + 1] = nums[i] + pre_sum[i]
        
        max_len = 0
        
        sum_idx = {}
        for idx, s in enumerate(pre_sum):
            if s not in sum_idx:
                sum_idx[s] = idx
            
            if (s - k) in sum_idx:
                max_len = max(max_len, idx - sum_idx[s - k])
            
        return max_len