class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = set() 
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    
                    left += 1
                    right -= 1
                    
        return [list(triplet) for triplet in res]