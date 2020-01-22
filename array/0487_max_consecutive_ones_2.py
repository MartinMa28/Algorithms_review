class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        '''
        1 0 1 1 0
        '''
        zero_idx = -1
        i = 0
        ones_len = 0
        max_len = 0
        
        while i < len(nums):
            if nums[i] == 1:
                ones_len += 1
                max_len = max(max_len, ones_len)
            else:
                if zero_idx == -1:
                    zero_idx = i
                    ones_len += 1
                    max_len = max(max_len, ones_len)
                else:
                    ones_len = i - zero_idx
                    zero_idx = i
                    
            i += 1
        
        return max_len