class Solution:
    
    def _common_prefix(self, str1, str2):
        c_prefix = ''
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                c_prefix += str1[i]
            else:
                break
                
        return c_prefix
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        c_prefix = self._common_prefix(strs[0], strs[1])
        
        for i in range(2, len(strs)):
            if strs[i].startswith(c_prefix):
                continue
            else:
                c_prefix = self._common_prefix(c_prefix, strs[i])
                if c_prefix == '':
                    return ''
                
        return c_prefix