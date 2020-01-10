from math import ceil

class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        """
        pick as much words as possible, each word is followed by a space
        """
        res = []
        i = 0
        
        while i < len(words):
            line_len = len(words[i])
            line_words = [words[i]]
            i += 1
            
            while i < len(words) and line_len + len(words[i]) + 1 <= maxWidth:
                line_len = line_len + len(words[i]) + 1
                line_words.append(words[i])
                i += 1
                
            
            if i < len(words):
                line = ''
                num_spaces = maxWidth - sum([len(w) for w in line_words])
                num_chunks = len(line_words) - 1
                
                for w in line_words:
                    line += w
                    if num_chunks > 0: 
                        line += ' ' * ceil(num_spaces / num_chunks)
                        num_spaces -= ceil(num_spaces / num_chunks)
                        num_chunks -= 1
                
                line += ' ' * (maxWidth - len(line))
            else:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            
            res.append(line)
        return res

def justify(s, max_width):
    words = []
    left = 0
    right = 0

    while left < len(s) and right < len(s):
        if s[right].isalpha():
            right += 1
        else:
            if s[left:right]:
                words.append(s[left:right])

            if s[right] == '\n':
                words.append('\n')

            right += 1
            left = right
    
    words.append(s[left:right])

    res = []
    i = 0

    while i < len(words):
        line_len = words[i]
        line_words = [words[i]]
        i += 1

        while i < len(words) and line_len + 1 + len(words[i]) <= max_width:
            if words[i] == '\n':
                i += 1
                break

            line_len += (1 + len(words[i]))
            line_words.append(words[i])
            i += 1

        if i < len(words):
            line = ''
            num_spaces = max_width - sum([len(w) for w in line_words])
            num_chunks = len(line_words) - 1

            for w in line_words:
                if num_chunks > 0:
                    line += w
                    line += ' ' * ceil(num_spaces / num_chunks)
                    num_spaces -= ceil(num_spaces / num_chunks)
                    num_chunks -= 1
            
            line += ' ' * (max_width - len(line))
            res.append(line)

            if words[i] == '\n':
                i += 1
        else:
            line = ' '.join(line_words)
            line += ' ' * (max_width - len(line))

            res.append(line)

    
    return res

        
justify('hello, world\n,Maritn', 12)