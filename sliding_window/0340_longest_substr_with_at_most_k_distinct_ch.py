class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        distin = {}
        
        if k == 0:
            return 0
        
        while right < len(s):
            if s[right] in distin:
                distin[s[right]] += 1
                max_len = max((max_len, right - left + 1))
                right += 1

            elif len(distin) < k:
                distin[s[right]] = 1
                max_len = max((max_len, right - left + 1))
                right += 1
            else:
                distin[s[left]] -= 1
                if distin[s[left]] == 0:
                    distin.pop(s[left])
                left += 1
                    
        return max_len

if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLongestSubstringKDistinct('eceba', 2))