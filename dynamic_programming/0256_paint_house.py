class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def _min_cost(self, color_idx: int, house_idx: int) -> int:
        if (color_idx, house_idx) in self.memo:
            return self.memo[(color_idx, house_idx)]
        
        if house_idx == len(self.costs) - 1:
            self.memo[(color_idx, house_idx)] = self.costs[house_idx][color_idx]
            return self.costs[house_idx][color_idx]
        
        min_cost = float('inf')
        color_cost = self.costs[house_idx][color_idx]
        
        for next_color in range(3):
            if next_color != color_idx:
                min_cost = min((min_cost, color_cost + self._min_cost(next_color, house_idx + 1)))
        
        
        self.memo[(color_idx, house_idx)] = min_cost
        return min_cost
        
    
    def minCost(self, costs: list) -> int:
        if costs == []:
            return 0
        
        self.costs = costs
        
        min_cost = float('inf')
        house_idx = 0
        
        for color_idx in range(3):
            min_cost = min((min_cost, self._min_cost(color_idx, house_idx)))
            
        return min_cost


    def minCost_bottom_up(self, costs: list) -> int:
        if costs == []:
            return 0
        
        dp = [[0 for _ in range(3)] for _ in range(len(costs))]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        for house in range(1, len(costs)):
            dp[house][0] = min((dp[house - 1][1], dp[house - 1][2])) \
                            + costs[house][0]
            dp[house][1] = min((dp[house - 1][0], dp[house - 1][2])) \
                            + costs[house][1]
            dp[house][2] = min((dp[house - 1][0], dp[house - 1][1])) \
                            + costs[house][2]
            
        return min(dp[-1])