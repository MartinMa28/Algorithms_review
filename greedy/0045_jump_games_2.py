class Solution:
    def jump(self, nums: list) -> int:
        right_most = 0
        jumps = 0
        cur_idx = 0
        
        for i in range(len(nums) - 1):
            right_most = max((right_most, i + nums[i]))
            
            if i == cur_idx:
                jumps += 1
                cur_idx = right_most
                
        return jumps