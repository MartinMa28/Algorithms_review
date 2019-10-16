class Solution:
    def __init__(self):
        self.results = []


    def _dfs(self, remaining: list, seq: list) -> None:
        if len(remaining) == 0:
            self.results.append(seq.copy())

        for idx, n in enumerate(remaining):
            seq.append(n)
            new_remaining = remaining[:idx] + remaining[idx + 1:]
            self._dfs(new_remaining, seq)
            
            # backtracking
            seq.pop()


    def permute(self, nums: list) -> list:
        self._dfs(nums, [])

        return self.results


if __name__ == "__main__":
    solu = Solution()
    print(solu.permute([1, 2, 3, 4]))
