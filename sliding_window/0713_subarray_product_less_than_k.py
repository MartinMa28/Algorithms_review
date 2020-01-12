class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        100
        10 5 2 6
        
           l
               r
        
        [[10], [10, 5], [5], [5, 2], [2], [5, 2, 6], [2, 6], [6]]
        '''
        if not nums:
            return 0
        
        if k <= 1:
            return 0
        
        left = 0
        right = 0
        cur_prod = 1
        cnt = 0
        
        while right < len(nums):
            cur_prod *= nums[right]
            
            while cur_prod >= k:
                cur_prod /= nums[left]
                left += 1
                
            cnt += (right - left) + 1
            right += 1
            
        return cnt