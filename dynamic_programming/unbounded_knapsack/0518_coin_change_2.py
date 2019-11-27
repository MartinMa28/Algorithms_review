class Solution:
    def __init__(self):
        self.memo = {}
        
    def _change(self, amount, coins, idx):
        if (amount, idx) in self.memo:
            return self.memo[(amount, idx)]
        
        if amount == 0:
            self.memo[(amount, idx)] = 1
            return 1
        elif amount < 0:
            return 0
        else:
            if idx == len(coins):
                self.memo[(amount, idx)] = 0
                return 0
            
            with_coin = self._change(amount - coins[idx], coins, idx)
            without_coin = self._change(amount, coins, idx + 1)
            
            self.memo[(amount, idx)] = with_coin + without_coin
            return with_coin + without_coin
        
    def change_top_down(self, amount, coins):
        return self._change(amount, coins, 0)


    def change(self, amount, coins):
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        for i in range(len(coins) + 1):
            dp[i][0] = 1
            
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[-1][-1]