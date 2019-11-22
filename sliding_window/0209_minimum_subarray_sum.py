class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        subarr_sum = 0
        left = 0
        right = 0
        
        min_len = float('inf')
        
        while right < len(nums):
            while subarr_sum < s and right < len(nums):     
                subarr_sum += nums[right]
                right += 1

            if subarr_sum >= s:
                if right - left < min_len:
                    min_len = right - left
                    print(left, right)
                
            
            while subarr_sum >= s:
                if right - left < min_len:
                    min_len = right - left
                    print(left, right)
                
                subarr_sum -= nums[left]
                left += 1
                
        
        if min_len == float('inf'):
            return 0
        
        return min_len