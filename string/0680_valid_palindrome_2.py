class Solution:
    def _check(self, s, left, right):
        if left < right:
            if s[left] != s[right]:
                return False, left, right
            else:
                return self._check(s, left + 1, right - 1)
        else:
            return True, left, right
    
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        is_palin, left, right = self._check(s, left, right)
        
        if is_palin:
            return True
        else:
            inc_left, _, _ = self._check(s, left + 1, right)
            dec_right, _, _ = self._check(s, left, right - 1)
            
            return inc_left or dec_right
