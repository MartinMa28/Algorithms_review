class Solution:
    def permute(self, nums: list) -> list:
        res = []

        def _backtrack(nums: list, seq: list) -> None:
            if len(nums) == 0:
                res.append(seq)
            else:
                for idx, n in enumerate(nums):
                    _backtrack(nums[:idx] + nums[idx + 1:], seq + [n])

        _backtrack(nums, [])

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.permute([1, 2, 3]))
