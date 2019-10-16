class Solution:
    def __init__(self):
        self.combs = []

    def _dfs(self, cur_num, cur_comb, n, k):
        if k - len(cur_comb) > n - cur_num + 1:
            return
        else:
            if len(cur_comb) == k:
                if cur_comb not in self.combs:
                    self.combs.append(cur_comb.copy())
            else:
                for num in range(cur_num + 1, n + 1):
                    cur_comb.append(num)
                    self._dfs(num, cur_comb, n, k)
                    # backtracking
                    cur_comb.pop()
            

    def combine(self, n: int, k: int) -> list:
        self._dfs(0, [], n, k)

        return self.combs


if __name__ == "__main__":
    solu = Solution()
    print(solu.combine(4, 3))