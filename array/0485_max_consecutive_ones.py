class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max_ones = 0
        cur_con = 0
        
        for n in nums:
            if n == 1:
                cur_con += 1
                max_ones = max(max_ones, cur_con)
            else:
                cur_con = 0
        
        return max_ones