class Solution:
    def __init__(self):
        self.reach = {}

    def _can_jump(self, idx):
        if idx in self.reach:
            return self.reach[idx]
        else:
            if self.nums[idx] >= len(self.nums) - 1 - idx:
                self.reach[idx] = True
                return True
            else:
                for i in range(self.nums[idx]):
                    if self._can_jump(idx + i + 1):
                        return True
                
                self.reach[idx] = False
                return False
    
    def canJump(self, nums: list) -> bool:
        self.nums = nums

        return self._can_jump(0)

    def canJump_bottom_up(self, nums: list) -> bool:
        memo = ['unknown' for _ in range(len(nums))]
        memo[-1] = 'good'

        for i in range(len(nums) - 2, -1, -1):
            furthest = min((i + nums[i], len(nums) - 1))
            for j in range(i + 1, furthest + 1):
                if memo[j] == 'good':
                    memo[i] = 'good'
                    break

        return memo[0] == 'good'

    def canJump_greedy(self, nums: list) -> bool:
        left_most_good = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= left_most_good:
                left_most_good = i
        
        return left_most_good == 0


if __name__ == "__main__":
    solu = Solution()

    print(solu.canJump_bottom_up([2, 3, 1, 1, 4]))
        