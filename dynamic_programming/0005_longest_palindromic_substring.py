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

    def __init__(self):
        self.LCS = ''
        self.memo = {}
    
    def longestPalindrome_top_down(self, s: str) -> str:
        if s == '':
            return s
        
        self._LCS(s, 0, len(s) - 1)
        
        if len(set(s)) == 1:
            return s
        
        return self.LCS
        
    
    def _LCS(self, s, i, j) -> bool:
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i == j:
            if len(self.LCS) < 1:
                self.LCS = s[i]
            
            self.memo[(i, j)] = True
            return True
        elif i > j:
            
            self.memo[(i, j)] = True
            return True
        else:
            if s[i] == s[j] and self._LCS(s, i + 1, j - 1):
                if len(self.LCS) < j - i + 1:
                    self.LCS = s[i:j + 1]

                self.memo[(i, j)] = True
                return True
            else:
                self._LCS(s, i + 1, j)
                self._LCS(s, i, j - 1)
                
                self.memo[(i, j)] = False
                return False

if __name__ == "__main__":
    solu = Solution()
    print(solu.longestPalindrome('babad'))
