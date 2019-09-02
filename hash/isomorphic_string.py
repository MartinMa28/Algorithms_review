class Solution:
    def _iso_encoding(self, s):
        cache = {}
        enc = []
        for ch in s:
            if ch not in cache:
                cache[ch] = len(cache) + 1
            
            enc.append(cache[ch])
        
        return enc

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_enc = self._iso_encoding(s)
        t_enc = self._iso_encoding(t)

        return s_enc == t_enc


if __name__ == "__main__":
    solu = Solution()
    print(solu.isIsomorphic('add', 'egg'))