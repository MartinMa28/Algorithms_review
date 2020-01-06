from collections import defaultdict

class Solution:
    
    @staticmethod
    def _cover(s_cnt, t_cnt):
        for ch in t_cnt:
            if t_cnt[ch] > s_cnt[ch]:
                return False
        
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        s_cnt = defaultdict(int)
        t_cnt = {}
        
        for ch in t:
            t_cnt[ch] = t_cnt.get(ch, 0) + 1
            
        left = 0
        right = 0
        res = ''
        min_len = float('inf')
        
        while left < len(s) and right < len(s):
            if not self._cover(s_cnt, t_cnt):
                s_cnt[s[right]] += 1
                right += 1
            else:
                if right - left < min_len:
                    min_len = (right - left)
                    res = s[left:right]
                    
                s_cnt[s[left]] -= 1
                left += 1
        
        while left < len(s) and self._cover(s_cnt, t_cnt):
            if right - left < min_len:
                min_len = (right - left)
                res = s[left:right]

            s_cnt[s[left]] -= 1
            left += 1
        
        return res
        
        
if __name__ == "__main__":
    solu = Solution()
    print(solu.minWindow('ADOBECODEBANC', 'ABC'))