from collections import defaultdict

class Solution:
    
    @staticmethod
    def _cover(s_map, t_map):
        for key in t_map:
            if key in s_map and s_map[key] >= t_map[key]:
                continue
            else:
                return False
        
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        
        for ch in t:
            t_map[ch] += 1
            
        left = 0
        right = 0
        min_len = float('inf')
        res = ''
        
        while left < len(s) and right < len(s):
            while not self._cover(s_map, t_map) and right < len(s):
                s_map[s[right]] += 1
                right += 1
            
            while self._cover(s_map, t_map):
                if right - left < min_len:
                    res = s[left: right]
                    min_len = right - left
                
                s_map[s[left]] -= 1
                left += 1
                
        return res
        
        
if __name__ == "__main__":
    solu = Solution()
    print(solu.minWindow('ADOBECODEBANC', 'ABC'))