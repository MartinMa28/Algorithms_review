class Solution:
    def maxProfit(self, prices: list) -> int:
        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        if changes == []:
            # only has one day transaction
            return 0

        max_profit = 0
        for c in changes:
            if c > 0:
                max_profit += c

        return max_profit
