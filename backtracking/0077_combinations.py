class Solution:
    def _dfs(self, k, cur_comb, nums, combs) -> None:
        if len(cur_comb) == k:
            combs.append(cur_comb.copy())
            return
        else:
            for idx, cur_num in enumerate(nums):
                if k - len(cur_comb) <= len(nums):
                    # There are enough numbers to combine together.
                    cur_comb.append(cur_num)
                    self._dfs(k, cur_comb, nums[idx + 1:], combs)
                    cur_comb.pop()
    
    def combine(self, n: int, k: int) -> list:
        combs = []
        self._dfs(k, [], list(range(1, n + 1)), combs)
        
        return combs


if __name__ == "__main__":
    solu = Solution()
    print(solu.combine(5, 2))