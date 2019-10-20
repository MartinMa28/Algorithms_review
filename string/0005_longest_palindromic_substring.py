class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        length = len(s)
        longest_pal = ''
        for i in range(2 * length - 1):
            # get the index of center
            if i % 2 == 0:
                left = i // 2 - 1
                right = i // 2 + 1
            else:
                left = i // 2
                right = i // 2 + 1
                
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    if right - left + 1 > len(longest_pal):
                        longest_pal = s[left : right + 1]
                    left -= 1
                    right += 1
                else:
                    break
                    
        if longest_pal == "":
            longest_pal = s[0]
        
        return longest_pal


if __name__ == "__main__":
    test = 'babad'
    solu = Solution()
    print(solu.longestPalindrome(test))