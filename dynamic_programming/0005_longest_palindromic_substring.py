class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        max_len = 1
        palin = s[0]
        for j in range(1, len(s)):
            for i in range(0, j):
                if dp[i + 1][j - 1] > 0:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                        if dp[i][j] > max_len:
                            max_len = dp[i][j]
                            palin = s[i: j + 1]
                else:
                    if i + 1 > j - 1 and s[i] == s[j]:
                        dp[i][j] = 2
                        if dp[i][j] > max_len:
                            max_len = dp[i][j]
                            palin = s[i: j + 1]
                
        
        
        return palin

if __name__ == "__main__":
    solu = Solution()
    print(solu.longestPalindrome('babad'))
