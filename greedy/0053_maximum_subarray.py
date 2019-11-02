class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        largest = -float('inf')
        for n in nums:
            curr += n
            
            if n > curr:
                curr = n
            
            largest = max((curr, largest))
            
        return largest