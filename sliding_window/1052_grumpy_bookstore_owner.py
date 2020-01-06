class Solution:
    """
    [1, 0, 1, 2, 1, 1, 7, 5]
    [0, 1, 0, 1, 0, 1, 0, 1]
    [0, 0, 0, 2, 0, 1, 0, 5]
    """
    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:
        improve = [customers[i] * grumpy[i] for i in range(len(customers))]
        window_sum = sum(improve[:X])
        max_sum = window_sum
        
        for i in range(len(customers) - X):
            window_sum = window_sum - improve[i] + improve[i + X]
            max_sum = max((max_sum, window_sum))
            
        original_sat = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                original_sat += customers[i]
                
        return original_sat + max_sum
        
        