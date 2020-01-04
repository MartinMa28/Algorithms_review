class Solution:
            
    def wordBreak(self, s: str, wordDict: list) -> list:
        memo = {}
        
        def _backtrack(s, words) -> list:
            if not s:
                return []
            
            if s in memo:
                return memo[s]
            
            res = []
            for w in words:
                if s == w:
                    res.append(w)
                elif s.startswith(w):
                    for w_break in _backtrack(s[len(w):], words):
                        res.append(' '.join((w, w_break)))
            
            memo[s] = res
            return res
        
        return _backtrack(s, wordDict)
        