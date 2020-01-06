class Solution:
    
    @staticmethod
    def _encode(word):
        enc = []
        
        idx = 0
        repeat = 0
        prev = None
        
        while idx < len(word):
            if word[idx] == prev:
                idx += 1
                repeat += 1
            else:
                if prev:
                    enc.append((prev, repeat))
                    
                prev = word[idx]
                repeat = 1

                idx += 1
                    
        
        if prev:
            enc.append((prev, repeat))
            
        return enc
                
    @staticmethod
    def _is_expressive(enc_s, enc_w):
        if len(enc_s) != len(enc_w):
            return False
        else:
            for i in range(len(enc_s)):
                ch_s = enc_s[i]
                ch_w = enc_w[i]
                
                if ch_s[0] == ch_w[0] and \
                    (ch_s[1] == ch_w[1] or (ch_s[1] >= ch_w[1] and ch_s[1] >= 3)):
                    continue
                else:
                    return False
                
            return True
        
    
    def expressiveWords(self, S: str, words: list) -> int:
        """
        helllooo
        hello, hellllo
        """
        enc_s = self._encode(S)
        cnt = 0
        print(enc_s)
        for w in words:
            enc_w = self._encode(w)
            print(enc_w)
            cnt += self._is_expressive(enc_s, enc_w)
            
        return cnt