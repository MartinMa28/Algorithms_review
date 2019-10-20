class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if strs == []:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        com_prefix = ''
        
        for i in range(min(map(lambda s: len(s), strs))):
            ch = strs[0][i]
            common = True
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    common = False
                    break
                
            if common:
                com_prefix += ch
            else:
                break
                
        return com_prefix