class Solution:
    def __init__(self):
        self.memo = {}
    
    def numDecodings(self, s: str) -> int:
        if s in self.memo:
            return self.memo[s]
        else:
            if s == '':
                self.memo[s] = 1
                return self.memo[s]

            if s[0] == '0':
                self.memo[s] = 0
                return self.memo[s]

            if len(s) >= 2 and int(s[:2]) <= 26:
                self.memo[s] = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
                return self.memo[s]
            else:
                self.memo[s] = self.numDecodings(s[1:])
                return self.memo[s]
                