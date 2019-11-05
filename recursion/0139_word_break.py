class Solution:
    def __init__(self):
        self.memo = {}
    
    def _dfs(self, s, word_dict):
        if s == '':
            return True
        
        for w in word_dict:
            if len(s) >= len(w):
                if s in self.memo:
                    return self.memo[s]
                elif s[:len(w)] == w and self._dfs(s[len(w):], word_dict):
                    self.memo[s] = True
                    return True
        
        self.memo[s] = False
        return False
    
    def wordBreak(self, s: str, wordDict: list) -> bool:
        return self._dfs(s, wordDict)