class Solution:
    def __init__(self):
        self.memo = {}
    
                
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        else:
            if s1 == s2:
                self.memo[(s1, s2)] = True
                return True
            
            for i in range(1, len(s1)):
                if self.isScramble(s1[:i], s2[:i]) and\
                    self.isScramble(s1[i:], s2[i:]):
                    self.memo[(s1, s2)] = True
                    return True
                
                if self.isScramble(s1[:i], s2[len(s2) - i:]) and\
                    self.isScramble(s1[i:], s2[:len(s2) - i]):
                    self.memo[(s1, s2)] = True
                    return True
            
            self.memo[(s1, s2)] = False
            
            return False