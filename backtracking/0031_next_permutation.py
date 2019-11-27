class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        backtrack = -1
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                backtrack = i - 1
                break
        
        if backtrack == -1:
            for i in range(len(nums) // 2):
                nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
        else:
            least_larger = -1
            for i in range(len(nums) - 1, backtrack, -1):
                if nums[i] > nums[backtrack]:
                    least_larger = i
                    break
                    
            nums[least_larger], nums[backtrack] = nums[backtrack], nums[least_larger]
            
            
            left_behind = nums[backtrack + 1:]
            left_behind.sort()
            
            for i in range(backtrack + 1, len(nums)):
                nums[i] = left_behind[i - backtrack - 1]
                
        