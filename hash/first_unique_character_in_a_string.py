from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_to_idx = OrderedDict()
        met = set()
        for idx, ch in enumerate(s):
            if ch not in met:
                ch_to_idx[ch] = idx
                met.add(ch)
            else:
                if ch in ch_to_idx:
                    ch_to_idx.pop(ch)

        if len(ch_to_idx) > 0:
            return ch_to_idx.popitem(last=False)[1]
        else:
            return -1 
                

if __name__ == "__main__":
    solu = Solution()
    print(solu.firstUniqChar("loveleetcode"))