import math

class Solution:
    def __init__(self):
        self.ans = []
    
    def _backtrack(self, n, cur_comb, start_factor):
        if n == 1:
            self.ans.append(cur_comb[:])
            return
        
        for i in range(start_factor, n + 1):
            if n % i == 0:
                cur_comb.append(i)
                self._backtrack(n // i, cur_comb, i)
                
                # backtracking
                cur_comb.pop()
                
            
    def getFactors(self, n: int) -> list:
        self._backtrack(n, [], 2)
        self.ans.pop()
        return self.ans

    # with trimming
    def _backtrack_trimming(self, n, cur_comb, start_factor):
        for i in range(start_factor, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                cur_comb.append(i)
                cur_comb.append(n // i)
                self.ans.append(cur_comb[:])
                cur_comb.pop()
                
                self._backtrack_trimming(n // i, cur_comb, i)
                
                # backtracking
                cur_comb.pop()
                    
    # with trimming
    def getFactors_trimming(self, n: int) -> list:
        self._backtrack_trimming(n, [], 2)
        return self.ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.getFactors(32))