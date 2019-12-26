class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        """
        pick as much words as possible, each word is followed by a space
        """
        res = []
        word_idx = 0
        
        while True:
            chars = len(words[word_idx])
            line = [words[word_idx]]
            word_idx += 1
            
            # include as many words as possible for this line
            while word_idx < len(words) and chars + len(words[word_idx]) + 1 <= maxWidth:
                chars += len(words[word_idx]) + 1
                line.append(words[word_idx])
                word_idx += 1
            
            # If it's not the last line, add spaces between words
            if word_idx < len(words):
                spaces = maxWidth - sum([len(w) for w in line])
                s_line = ''
                num_spaces = len(line) - 1
                
                for w in line:
                    s_line += w
                    if num_spaces > 0:
                        space_len = spaces // num_spaces + (spaces % num_spaces > 0)
                        s_line += ' ' * space_len
                        spaces -= space_len
                        num_spaces -= 1
                
                res.append(s_line + ' ' * (maxWidth - len(s_line)))
            else:
                # In the last line, don't add extra spaces, and break the while loop.
                s_line = ' '.join(line)
                s_line += ' ' * (maxWidth - len(s_line))
                res.append(s_line)
                break
                
        return res