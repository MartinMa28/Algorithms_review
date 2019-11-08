class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        if len(s) == len(t):
            # replace
            differ = False
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                else:
                    if not differ:
                        differ = True
                    else:
                        return False
            
            return True
        else:
            if len(s) > len(t):
                s, t = t, s
            
            if len(t) - len(s) != 1:
                return False
            
            # s is short than t
            i = 0
            j = 0
            differ = False
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    if not differ:
                        j += 1
                        differ = True
                    else:
                        return False
            
                    
            return True