class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        queue = s.split()
        
        reversed_words = []
        while queue:
            reversed_words.append(queue.pop())
            
        return ' '.join(reversed_words)