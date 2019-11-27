class Solution:
    
    def _count_str(self, s):
        cnt = [0] * 26
        
        for ch in s:
            offset = ord(ch) - ord('a')
            cnt[offset] += 1
            
        return tuple(cnt)
    
    def groupAnagrams(self, strs: list) -> list:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        
        for word in strs:
            word_cnt = self._count_str(word)
            if word_cnt in group:
                group[word_cnt].append(word)
            else:
                group[word_cnt] = [word]
                
                
        return [wd for wd in group.values()]