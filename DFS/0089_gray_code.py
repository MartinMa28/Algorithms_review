class Solution:
    def __init__(self):
        self.ans = []
        
    @staticmethod
    def _binary_to_int(t_num):
        decimal = 0
        for i in range(len(t_num)):
            decimal += t_num[i] * (2 ** i)
            
        return decimal
        
    def _dfs(self, num: tuple, seen):
        if num not in seen:
            self.ans.append(self._binary_to_int(num))
            seen.add(num)
        
            for i in range(len(num)):
                bit = num[i]
                next_bit = 1 - bit
                self._dfs(num[:i] + (next_bit,) + num[i + 1:], seen)
                
        
    
    def grayCode(self, n: int) -> list:
        n = tuple([0 for _ in range(n)])
        seen = set()
        self._dfs(n, seen)
        
        return self.ans