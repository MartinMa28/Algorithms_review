class Solution:
    
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ch_map = {}
        max_len = 0
        sub_str = ''
        idx = 0
        
        while idx < len(s): 
            if s[idx] in ch_map:
                sub_str += s[idx]
                ch_map[s[idx]] += 1
                idx += 1
            elif len(ch_map) < 2:
                sub_str += s[idx]
                ch_map[s[idx]] = 1
                idx += 1
            else:
                popped_ch = sub_str[0]
                sub_str = sub_str[1:]
                ch_map[popped_ch] -= 1
                if ch_map[popped_ch] == 0:
                    ch_map.pop(popped_ch)
            
            max_len = max((max_len, len(sub_str)))
        
        return max_len
                
        
if __name__ == "__main__":
    so = Solution()
    print(so.lengthOfLongestSubstringTwoDistinct("abaccc"))