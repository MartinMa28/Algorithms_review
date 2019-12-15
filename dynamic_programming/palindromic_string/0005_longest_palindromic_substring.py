class Solution:
    def __init__(self):
        self.memo = {}
        self.lps = ''
    
    def _lps(self, s, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i == j:
            if len(self.lps) < j - i + 1:
                self.lps = s[i]
            return True
        elif i > j:
            return True
        else:
            if s[i] == s[j] and self._lps(s, i + 1, j - 1):
                if len(self.lps) < j - i + 1:
                    self.lps = s[i:j + 1]

                self.memo[(i, j)] = True
                return True
            else:
                self._lps(s, i + 1, j)
                self._lps(s, i , j - 1)
                
                self.memo[(i, j)] = False
                return False
                        
            
    
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return s
        
        if len(set(s)) == 1:
            return s
        
        self._lps(s, 0, len(s) - 1)
        return self.lps
        