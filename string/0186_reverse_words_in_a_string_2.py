class Solution:
    
    def _swap(self, s, i, j):
        s[i], s[j] = s[j], s[i]
        
    def _swap_by_range(self, s, start_idx, end_idx):
        if start_idx < end_idx:
            self._swap(s, start_idx, end_idx)
            self._swap_by_range(s, start_idx + 1, end_idx - 1)
    
    def reverseWords(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        else:
            self._swap_by_range(s, 0, len(s) - 1)
            
            # swap each back to the correct spell
            left = 0
            right = left + 1
            
            while left <= len(s) - 1 and right <= len(s) - 1:
                if s[right] == ' ':
                    self._swap_by_range(s, left, right - 1)
                    left = right + 1
                    right = right + 2
                else:
                    right += 1
                    
            # swap the last word
            self._swap_by_range(s, left, right - 1)