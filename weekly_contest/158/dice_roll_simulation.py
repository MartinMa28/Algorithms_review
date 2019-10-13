class Solution:
    def __init__(self):
        self.cnt = 0

    def _help(self, n: int, times: int, cur_roll: list, prev: int, con: int):
        for idx, r in enumerate(cur_roll):
            if idx != prev or con < r:
                if n == times:
                    self.cnt += 1
                else:
                    if idx != prev:
                        self._help(n + 1, times, cur_roll, idx, 1)
                    else:
                        self._help(n + 1, times, cur_roll, idx, con + 1)
                

    def dieSimulator(self, n: int, rollMax: list) -> int:
        self._help(1, n, rollMax, 7777, 1)

        return int(self.cnt % (1e9 + 7))


if __name__ == "__main__":
    solu = Solution()
    print(solu.dieSimulator(10, [1,2,2,2,2,3]))
        