class Solution:
    def __init__(self):
        self.memo = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(5000)]

    def _dfs(self, times_left: int, roll_max: list, prev: int, conti_len: int):
        ans = 0

        for idx, r in enumerate(roll_max):
            if idx != prev or conti_len < r:
                if times_left == 0:
                    return 1
                else:
                    if idx != prev:
                        if self.memo[times_left - 1][idx][1] > 0:
                            ans += self.memo[times_left - 1][idx][1]
                        else:
                            self.memo[times_left - 1][idx][1] = \
                                int(self._dfs(times_left - 1, roll_max, idx, 1) % (1e9 + 7))
                            ans += self.memo[times_left - 1][idx][1]
                    else:
                        if self.memo[times_left - 1][idx][conti_len + 1] > 0:
                            ans += self.memo[times_left - 1][idx][conti_len + 1]
                        else:
                            self.memo[times_left - 1][idx][conti_len + 1] = \
                                int(self._dfs(times_left - 1, roll_max, idx, conti_len + 1) % (1e9 + 7))
                            ans += self.memo[times_left - 1][idx][conti_len + 1]

        return int(ans % (1e9 + 7))
                

    def dieSimulator(self, n: int, rollMax: list) -> int:

        return self._dfs(n, rollMax, 7777, 1)


if __name__ == "__main__":
    solu = Solution()
    print(solu.dieSimulator(3000, [3,6,6,15,2,7]))
        