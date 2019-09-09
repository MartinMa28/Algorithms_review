class Solution:
    def __init__(self):
        self.cache = {}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]

        if N < 2:
            self.cache[N] = N
            return N

        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]