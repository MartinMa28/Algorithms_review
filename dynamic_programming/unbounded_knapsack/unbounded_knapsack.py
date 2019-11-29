class Solution:
    def __init__(self):
        self.memo = {}

    def solve_knapsack(self, profits, weights, capacity):
        if capacity in self.memo:
            return self.memo[capacity]
        
        if capacity == 0:
            self.memo[capacity] = 0
            return 0

        max_profit = 0

        for i in range(len(profits)):
            if weights[i] <= capacity:
                max_profit = max((max_profit, 
                profits[i] + self.solve_knapsack(profits, weights, capacity - weights[i])))
        
        self.memo[capacity] = max_profit
        return max_profit

if __name__ == "__main__":
    solu = Solution()

    print(solu.solve_knapsack([15, 20, 50], [1, 2, 3], 5))