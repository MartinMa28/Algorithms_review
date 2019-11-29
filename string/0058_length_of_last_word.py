class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        
        words = list(filter(lambda x: x != '', words))
        
        if len(words) == 0:
            return 0
        else:
            return len(words[-1])
        