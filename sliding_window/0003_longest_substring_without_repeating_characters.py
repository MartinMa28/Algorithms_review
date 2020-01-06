class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        
        left = 0
        right = 0
        ans = 0
        
        while left < len(s) and right < len(s):
            if s[right] not in ch_set:
                ch_set.add(s[right])
                ans = max((ans, right - left + 1))
                
                right += 1
            else:
                ch_set.discard(s[left])
                left += 1
        
        return ans