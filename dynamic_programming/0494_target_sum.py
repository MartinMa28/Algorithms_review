class Solution:
    def __init__(self):
        self.cnt = 0
        self.memo = {}
    
    def _top_down(self, nums, target, cur_idx) -> int:
        if (cur_idx, target) in self.memo:
            return self.memo[(cur_idx, target)]
        
        if cur_idx == len(nums):
            # Checked all of nums
            if target == 0:
                # Sums upto the target
                self.memo[(cur_idx, target)] = 1
                return 1
            else:
                self.memo[(cur_idx, target)] = 0
                return 0
        
        cnt = 0
        # minus symbol
        cnt += self._top_down(nums, target + nums[cur_idx], cur_idx + 1)
        # plus symbol
        cnt += self._top_down(nums, target - nums[cur_idx], cur_idx + 1)
        
        self.memo[(cur_idx, target)] = cnt
        
        return cnt
    
    
    def findTargetSumWays_top_down(self, nums: list, S: int) -> int:        
        return self._top_down(nums, S, 0)

    def findTargetSumWays(self, nums: list, S: int) -> int:
        pass
        