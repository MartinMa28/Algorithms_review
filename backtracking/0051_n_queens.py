class Solution:
    def __init__(self):
        self.ans = []
        self.cols = set()
        
    def _is_valid(self, queens, row, col):
        if col in self.cols:
            return False
        
        for q in queens:
            if abs(q[0] - row) / abs(q[1] - col) == 1:
                return False
        
        return True
    
    def _backtrack(self, queens, row, n):
        if row == n:
            self.ans.append(queens[:])
            return
        
        for col in range(n):
            if self._is_valid(queens, row, col):
                queens.append((row, col))
                self.cols.add(col)
                
                self._backtrack(queens, row + 1, n)
                
                # backtrack
                queens.pop()
                self.cols.discard(col)
            
    def _transform(self, queens):
        res = []
        
        for q in queens:
            line = '.' * q[1] + 'Q' + '.' * (len(queens) - 1 - q[1])
            res.append(line)
            
        return res
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self._backtrack([], 0, n)
        return map(self._transform, self.ans)
        
        

if __name__ == "__main__":
    solu = Solution()
    print(solu.solveNQueens(8))
    print(solu.results)