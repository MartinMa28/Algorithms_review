class Solution:
    def __init__(self):
        self.memo = {}
    
    def _recursive_exchange(self, coins: list, 
                                    amount: int) -> int:
        res = []
        for c in coins:
            if c == amount:
                if amount not in self.memo:
                    self.memo[amount] = 1
                    
                return 1
            elif c < amount:
                if (amount - c) not in self.memo:
                    sub_exchange = self._recursive_exchange(coins, amount - c)
                    self.memo[amount - c] = sub_exchange
                    
                if self.memo[amount - c] > 0:
                    res.append(self.memo[amount - c] + 1)
        
        if len(res) == 0:
            return -1
        else:
            return min(res)
        
      

    def coinChange(self, coins: list, amount: int) -> int:
        # Sort the coins in the descending order
        if amount == 0:
            return 0
        
        return self._recursive_exchange(coins, amount)
