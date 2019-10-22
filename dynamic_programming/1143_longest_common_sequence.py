class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        # Entries of the first row and col are equal to 0, because every string only has
        # 0 LCS with an empty string.
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # i denotes the i-th character in text1, j denotes the j-th character in text2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # If the trailing character is the same,
                    # LCS(text1[:i], text2[:j]) == 1 + LCS(text1[:i - 1], text2[:j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise LCS(text1[:i], text2[:j]) ==
                    # max(LCS(text1[:i], text2[:j - 1]), LCS(text1[:i - 1], text2[:j]))
                    dp[i][j] = max((dp[i][j - 1], dp[i - 1][j]))
        
        return dp[m][n]

if __name__ == "__main__":
    solu = Solution()
    solu.longestCommonSubsequence('ace', 'abcde')
