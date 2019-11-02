from collections import deque

class Solution:
    def _is_valid(self, hm, hm_t):
        for val, t_val in zip(hm.values(), hm_t.values()):
            if val < t_val:
                return False
            
        return True
    
    def _list_to_str(self, l):
        ret = ''
        for c in l:
            ret += c
            
        return ret
    
    def minWindow(self, s: str, t: str) -> str:
        hm_t = {}
        
        for ch in t:
            hm_t[ch] = hm_t.get(ch, 0) + 1
            
        if len(t) == 0 or s == '':
            return ''
        
        left = 0
        right = left
        hm = {}
        
        for k in hm_t:
            hm[k] = 0
        
        cur = deque()
        min_len = float('inf')
        min_s = ''
        
        while right <= len(s):
            if not self._is_valid(hm, hm_t):
                if right == len(s):
                    break
                cur.append(s[right])
                if s[right] in hm:
                    hm[s[right]] += 1

                right += 1
            else:
                while True:
                    if len(cur) < min_len:
                        min_len = len(cur)
                        min_s = self._list_to_str(cur)

                    popped = cur.popleft()
                    if popped in hm:
                        hm[popped] -= 1

                    if not self._is_valid(hm, hm_t):
                        break
            
        return min_s
        
        
if __name__ == "__main__":
    solu = Solution()
    print(solu.minWindow('ADOBECODEBANC', 'ABC'))