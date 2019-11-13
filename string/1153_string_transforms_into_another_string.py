class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # valid when characters in str1 
        # only map to a single character in str2
        
        ch_map = {}
        
        if len(set(str2)) == 26 and str1 != str2:
            return False
        
        for i in range(len(str1)):
            if str1[i] in ch_map:
                if ch_map[str1[i]] == str2[i]:
                    continue
                else:
                    return False
            else:
                ch_map[str1[i]] = str2[i]
                
        return True