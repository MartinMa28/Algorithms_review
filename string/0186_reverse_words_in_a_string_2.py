class Solution:
    
    def _reverse_by_range(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    
    def reverseWords(self, s: List[str]) -> None:
        """
        Firstly, reverse the whole string.
        And then reverse each word back to it's correct order.
        """
        self._reverse_by_range(s, 0, len(s) - 1)
        
        start = 0
        end = 0
        while end < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            
            self._reverse_by_range(s, start, end - 1)
            start = end + 1
            end = end + 1
        
        