class Solution:
    def findLength(self, A: list, B: list) -> int:
        '''
        1 2 3 2 1
        3 2 1 4 7
        
        i == j
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = 0
        '''
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        
        max_len = 0
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    max_len = max(max_len, dp[i + 1][j + 1])
                else:
                    dp[i + 1][j + 1] = 0
        
        return max_len