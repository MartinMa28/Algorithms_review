class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def _dfs(self, s, words) -> tuple:
        if s == '':
            return True, ['']
        
        if s in self.memo:
            return self.memo[s]
        
        ans = []
        for word in words:
            if s.startswith(word):
                found, word_break = self._dfs(s[len(word):], words)
                if found:
                    ans.extend([word + ' ' + wb for wb in word_break])

        self.memo[s] = len(ans) > 0, ans
        return len(ans) > 0, ans
                    
        
    def wordBreak(self, s: str, wordDict: list) -> list:
        ans = self._dfs(s, wordDict)[1]
        return [a[:-1] for a in ans]
                
        