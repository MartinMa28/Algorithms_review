class Solution:
    
    def _could_shift(self, from_str, to_str):
        if len(from_str) != len(to_str):
            return False
        
        from_unicode = [ord(ch) for ch in from_str]
        to_unicode = [ord(ch) for ch in to_str]
        
        steps = [(from_unicode[i] - to_unicode[i]) % 26 for i in range(len(from_str))]
        
        return len(set(steps)) == 1 
    
    def groupStrings(self, strings: list) -> list:
        if strings == []:
            return []
        
        group = [[strings[0]]]
        
        for word in strings[1:]:
            shiftable = False
            for g in group:
                if self._could_shift(g[0], word):
                    g.append(word)
                    shiftable = True
                    break
            
            if not shiftable:
                group.append([word])
                    
        return group
        
        