class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def _word_break(self, s: str) -> list:
        if s in self.memo:
            return self.memo[s]
        
        if s == '':
            return ['']
        
        res = []
        for i in range(len(s)):
            check = s[i:]
            if check in self.word_dict:
                sub_results = self._word_break(s[:i])
                
                res.extend([s_r + check + ' ' for s_r in sub_results])
            else:
                continue
        
        self.memo[s] = res
        return res
                
                
    
    def wordBreak(self, s: str, wordDict: list) -> list:
        self.word_dict = set(wordDict)
        return [ans[:-1] for ans in self._word_break(s)]