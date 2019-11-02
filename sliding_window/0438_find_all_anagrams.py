class Solution:
    def _is_anagram(self, map1, map2):
        for k in map1:
            if k in map2:
                if map1[k] != map2[k]:
                    return False
            else:
                return False
            
        return True
        
    
    def findAnagrams(self, s: str, p: str) -> list:
        map_p = {}
        for ch in p:
            map_p[ch] = map_p.get(ch, 0) + 1
        
        map_s = {}
        for ch in s[:len(p)]:
            map_s[ch] = map_s.get(ch, 0) + 1
        
        res = []
        
        if self._is_anagram(map_p, map_s):
            res.append(0)
            
        for i in range(1, len(s) -len(p) + 1):
            map_s[s[i - 1]] = map_s.get(s[i - 1]) - 1
            map_s[s[i + len(p) - 1]] = map_s.get(s[i + len(p) - 1], 0) + 1
            if self._is_anagram(map_p, map_s):
                res.append(i)
                
        return res