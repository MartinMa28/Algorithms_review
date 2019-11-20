class Solution:
    def __init__(self):
        self.memo = {}
    
    def integerBreak_top_down(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n <= 2:
            return 1
        
        max_prod = 0
        for i in range(1, n):
            max_prod = max((max_prod, i * (n - i)))
            max_prod = max((max_prod, i * self.integerBreak_top_down(n - i)))
            
        self.memo[n] = max_prod
        
        return max_prod

    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(3, n + 1):
            max_value = 0
            for j in range(1, i):
                max_value = max((max_value, j * (i - j)))
                max_value = max((max_value, j * dp[i - 1 - j]))
                
            dp[i - 1] = max_value
            
        return dp[-1]



if __name__ == "__main__":
    solu = Solution()
    print(solu.integerBreak(10))