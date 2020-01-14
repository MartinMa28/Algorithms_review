class Solution:
    
    @staticmethod
    def _idx(ch):
        return ord(ch) - ord('a')
    
    def numMatchingSubseq(self, S: str, words: list) -> int:
        matching_table = [[] for _ in range(26)]
        
        for w in words:
            matching_table[self._idx(w[0])].append(w)
        
        num_subseq = 0
        
        for ch in S:
            if matching_table[self._idx(ch)]:
                matches = matching_table[self._idx(ch)]
                matching_table[self._idx(ch)] = []
                while matches:
                    matching_word = matches.pop()
                    matching_word = matching_word[1:]
                    
                    if not matching_word:
                        num_subseq += 1
                    else:
                        matching_table[self._idx(matching_word[0])].append(matching_word)
        
        return num_subseq

if __name__ == "__main__":
    solu = Solution()
    print(solu.numMatchingSubseq('abcde', ["a", "bb", "acd", "ace"]))