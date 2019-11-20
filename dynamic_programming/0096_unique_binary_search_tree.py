class Solution:
    
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] += 2 * dp[i - j] * dp[j - 1]
                
            if i % 2 > 0:
                dp[i] += dp[i // 2] * dp[i // 2]
                
        return dp[-1]