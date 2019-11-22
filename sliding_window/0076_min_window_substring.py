class Solution:
    def _contains_all(self, t_dict, s_dict):
        for k in t_dict:
            if k in s_dict:
                if t_dict[k] > s_dict[k]:
                    return False
            else:
                return False
            
        return True

    
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        t_cnt = {}
        s_cnt = {}
        
        for ch in t:
            t_cnt[ch] = t_cnt.get(ch, 0) + 1
        
        left = 0
        right = 0
        
        min_substr = ''
        min_len = float('inf')
        
        while right < len(s):
            while not self._contains_all(t_cnt, s_cnt) and right < len(s):
                s_cnt[s[right]] = s_cnt.get(s[right], 0) + 1
                right += 1
            
            # right points to an extra character
            while self._contains_all(t_cnt, s_cnt):
                if (right - left) < min_len:
                    min_substr = s[left:right]
                    min_len = len(min_substr)
                
                s_cnt[s[left]] -= 1
                left += 1
                
                    
        return min_substr
        
        
if __name__ == "__main__":
    solu = Solution()
    print(solu.minWindow('ADOBECODEBANC', 'ABC'))