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
        
      

    def coinChange_top_down_memoizing(self, coins: list, amount: int) -> int:
        # Sort the coins in the descending order
        if amount == 0:
            return 0
        
        return self._recursive_exchange(coins, amount)

    
    def coinChange(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0
        
        l = [-1 for _ in range(amount)]
        l = [0] + l
        
        for i in range(1, amount + 1):
            candidates = []
            for c in coins:
                if c <= i and l[i - c] != -1:
                    candidates.append(l[i - c] + 1)
            
            if len(candidates) > 0:
                l[i] = min(candidates)
            
        return l[-1]
