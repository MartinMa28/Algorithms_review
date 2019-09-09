class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        if K % 2 == 1:
            return self.kthGrammar(N - 1, (K + 1) / 2)
        else:
            return self.kthGrammar(N - 1, K / 2) ^ 1