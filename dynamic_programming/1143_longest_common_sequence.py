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

    def __init__(self):
        self.memo = {}
    
    def longestCommonSubsequence_top_down(self, text1: str, text2: str) -> int:
        if (text1, text2) in self.memo:
            return self.memo[(text1, text2)]
        
        if text1 == text2:
            self.memo[(text1, text2)] = len(text1)
            return len(text1)
        
        if text1 == '' or text2 == '':
            self.memo[(text1, text2)] = 0
            return 0
        
        if text1[0] == text2[0]:
            res = self.longestCommonSubsequence(text1[1:], text2[1:]) + 1
            self.memo[(text1, text2)] = res
            return res
        else:
            keep_text1 = self.longestCommonSubsequence(text1, text2[1:])
            keep_text2 = self.longestCommonSubsequence(text1[1:], text2)
            
            self.memo[(text1, text2)] = max((keep_text1, keep_text2))
            return max((keep_text1, keep_text2))

if __name__ == "__main__":
    solu = Solution()
    solu.longestCommonSubsequence('ace', 'abcde')
