from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        left = 0
        right = 0
        
        delimiters = set(['!', '?', ',', ';', '.', "\'", ' '])
        banned = set([w.lower() for w in banned])
        paragraph = paragraph.strip()
        counter = defaultdict(int)
        max_freq = 0
        freq_word = ''
        
        while left < len(paragraph) and right < len(paragraph):
            if paragraph[left] in delimiters:
                left += 1
                right = left
            elif paragraph[right] not in delimiters:
                right += 1
            else:
                word = paragraph[left: right].lower()
                
                if word not in banned:
                    counter[word] += 1

                    if counter[word] > max_freq:
                        max_freq = counter[word]
                        freq_word = word
                
                left = right + 1
                right = left
                
        word = paragraph[left: right].lower()
        if word:
            if word not in banned:
                counter[word] += 1
                if counter[word] > max_freq:
                    max_freq = counter[word]
                    freq_word = word
                    
        return freq_word