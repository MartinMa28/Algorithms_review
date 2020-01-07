class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        src_set = set(list(source))
        ans = 1
        i = 0
        
        for idx, ch in enumerate(target):
            if ch not in src_set:
                return -1
            
            while source[i] != ch:
                i += 1
                
                if i == len(source):
                    ans += 1
                    i = 0
            
            i += 1
            if i == len(source) and idx != len(target) - 1:
                ans += 1
                i = 0
                
        return ans