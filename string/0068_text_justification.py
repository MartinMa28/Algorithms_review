class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        line_ch_cnt = 0
        line_words = []
        res = []
        word_idx = 0
        
        while word_idx < len(words):
            w = words[word_idx]
            
            if line_ch_cnt + len(w) <= maxWidth:
                line_words.append(w)
                line_ch_cnt += len(w) + 1
                word_idx += 1
            else:
                spaces = maxWidth - sum([len(w) for w in line_words])

                if len(line_words) == 1:
                    l = line_words[0] + ' ' * spaces
                    res.append(l)
                    line_words = []
                    line_ch_cnt = 0
                else:
                    avg_space = spaces / (len(line_words) - 1)

                    if int(avg_space) == avg_space:
                        # Spaces are evenly distributed.

                        l = ''
                        for w in line_words[:-1]:
                            l += w + ' ' * int(avg_space)
                        l += line_words[-1]

                        res.append(l)
                        line_words = []
                        line_ch_cnt = 0

                    else:
                        l = ''
                        for idx, w in enumerate(line_words):
                            if spaces == 0:
                                l += w
                            elif (spaces / (len(line_words) - 1 - idx)) % 1 > 0:
                                l += w + ' ' * (int(avg_space) + 1)
                                spaces -= int(avg_space) + 1
                            else:
                                l += w + ' ' * int(avg_space)
                                spaces -= int(avg_space)
                        res.append(l)
                        line_words = []
                        line_ch_cnt = 0
                        
        l = ''
        for w in line_words[:-1]:
            l += w + ' '
        
        l += line_words[-1]
        l += ' ' * (maxWidth - len(l))
        res.append(l)
                                
        return res