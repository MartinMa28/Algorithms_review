class Solution:
    def _is_permu(self, map1, map2):
        for k in map1:
            if k not in map2:
                return False
            else:
                if map1[k] != map2[k]:
                    return False
                
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map1 = {}
        for ch in s1:
            map1[ch] = map1.get(ch, 0) + 1
            
        map2 = {}
        for ch in s2[:len(s1)]:
            map2[ch] = map2.get(ch, 0) + 1
        
        idx = 0
        while True:
            if self._is_permu(map1, map2):
                return True
            
            map2[s2[idx]] -= 1
            
            if idx + len(s1) < len(s2):
                map2[s2[idx + len(s1)]] = map2.get(s2[idx + len(s1)], 0) + 1
                idx += 1
            else:
                break
                
        return False