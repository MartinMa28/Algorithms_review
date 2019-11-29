class Solution:

    def __init__(self):
        self.memo = {}

    def _count(self, nums, target, cur_idx):
        if (target, cur_idx) in self.memo:
            return self.memo[(target, cur_idx)]
        
        if target < 0:
            return 0
        elif target == 0:
            return 1
        else:
            if cur_idx == len(nums):
                return 0   

            with_cur_num = self._count(nums, target - nums[cur_idx], cur_idx + 1)
            without_cur_num = self._count(nums, target, cur_idx + 1)

            self.memo[(target, cur_idx)] = with_cur_num + without_cur_num
            return with_cur_num + without_cur_num

    def count_of_subset_sum(self, nums, target) -> int:
        return self._count(nums, target, 0)

    def count_of_subset_sum_bottom_up(self, nums, target) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    # this number doesn't exceed the target
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    # exceeds the target
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.count_of_subset_sum_bottom_up([1, 1, 2, 3], 4))