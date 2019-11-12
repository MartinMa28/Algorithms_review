class Solution:
    
    def _three_sum(self, nums, target):
        res = set()
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
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return [list(triplet) for triplet in res]
    
    
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        
        res = []
        for i in range(len(nums) - 3):
            sub_target = target - nums[i]
            sub_results = self._three_sum(nums[i + 1:], sub_target)
            
            ans_list = [[nums[i]] + triplet for triplet in sub_results]
            
            for ans in ans_list:
                if ans not in res:
                    res.append(ans)
            
        return res
        
        