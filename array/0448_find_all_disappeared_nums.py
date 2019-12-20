class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        for i, n in enumerate(nums):
            new_idx = abs(n) - 1
            nums[new_idx] = -abs(nums[new_idx])
            
        res = []
        
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
                
        return res