class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        dists = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        dists[i][j] = dists[i - 1][j - 1] + 1
                    else:
                        dists[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        dists[i][j] = max((dists[i][j - 1], dists[i - 1][j]))
                    elif i > 0 and j == 0:
                        dists[i][j] = dists[i - 1][j]
                    elif i == 0 and j > 0:
                        dists[i][j] = dists[i][j - 1]
                    else:
                        dists[i][j] = 0
        
        return dists[m - 1][n - 1]

if __name__ == "__main__":
    solu = Solution()
    solu.longestCommonSubsequence('ace', 'abcde')
