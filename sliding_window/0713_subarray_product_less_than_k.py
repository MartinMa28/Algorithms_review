class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        '''
        10  5  2  6            100
            l
                  r
               
               
        [10], [10 5], [5], [5 2], [5 2 6]. [2], [2 6], [6]
        '''
        if k <= 1:
            return 0
        
        prod = 1
        left = 0
        right = 0
        cnt = 0
        max_prod = prod
        
        while right < len(nums):
            prod *= nums[right]
            
            while prod >= k:
                prod /= nums[left]
                left += 1
            
            max_prod = max(max_prod, prod)
            
            cnt += (right - left) + 1
            right += 1
        
        print(max_prod)
        return cnt