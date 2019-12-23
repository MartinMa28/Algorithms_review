class Solution:

    def __init__(self):
        self.memo = {}
    
    def _can_jump(self, nums, pos) -> bool:
        if pos in self.memo:
            return self.memo[pos]
        
        if pos >= len(nums) - 1:
            return True
        
        for i in range(1, nums[pos] + 1):
            if self._can_jump(nums, pos + i):
                self.memo[pos] = True
                return True
        
        self.memo[pos] = False
        return False
        
    
    def canJump_top_down(self, nums: list) -> bool:
        return self._can_jump(nums, 0)

    def canJump_bottom_up(self, nums: list) -> bool:
        if len(nums) == 1:
            return True
        
        dp = [0] * len(nums)
        
        for pos in range(len(nums) - 1, -1, -1):
            for i in range(1, nums[pos] + 1):
                if pos + i >= len(nums) - 1 or dp[pos + i]:
                    dp[pos] = 1
                    
        return dp[0]

    def canJump_1d_DP(self, nums: list) -> bool:
        if len(nums) == 1:
            return True
        
        left_most_reachable = len(nums) - 1
        
        for pos in range(len(nums) - 2, -1, -1):
            if pos + nums[pos] >= left_most_reachable:
                left_most_reachable = pos
            
                    
        return left_most_reachable == 0

if __name__ == "__main__":
    solu = Solution()

    print(solu.canJump_bottom_up([2, 3, 1, 1, 4]))
        