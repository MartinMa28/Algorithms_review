class Solution:
    
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[-1]
        min_diff = abs(result - target)
        
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    return current_sum
                
                if abs(current_sum - target) < min_diff:
                    min_diff = abs(current_sum - target)
                    result = current_sum
                    
        return result