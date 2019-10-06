class Solution:
    def maxProfit(self, prices: list) -> int:
        min_price = float('inf')
        total_profit = 0
        profit = 0
        
        for p in prices:
            if p - min_price >= profit:
                # making more money, save the profit
                profit = p - min_price
            else:
                # Starting losing money or making less money, start a new transaction.
                # Update the min_price, total_profit, set profit to zero.
                min_price = p
                total_profit += profit
                profit = 0
            
        
        total_profit += profit
        
        return total_profit