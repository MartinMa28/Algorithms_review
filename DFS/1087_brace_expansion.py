class Solution:
    
    def _dfs(self, seq, cur, res):
        if not seq:
            res.append(cur)
        else:
            choice = seq[0]
            
            if len(choice) == 1:
                self._dfs(seq[1:], cur + choice, res)
            else:
                for ch in choice:
                    self._dfs(seq[1:], cur + ch, res)
                    
    
    def expand(self, S: str) -> list:
        stack = []
        seq = []
        i = 0
        
        while i < len(S):
            if S[i] == '{':
                choices = ''
                i += 1
                while S[i] != '}':
                    choices += S[i]
                    i += 1
                
                i += 1
                if len(choices) == 1:
                    seq.append(choices)
                else:
                    seq.append(sorted(choices.split(',')))
            else:
                seq.append(S[i])
                i += 1
        
        res = []
        self._dfs(seq, '', res)
        
        return res