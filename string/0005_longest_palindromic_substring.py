class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ''

        # to get 2n - 1 insertion positions, and exclude the len(s) - 0.5
        i = 0
        while i <= len(s) - 1:
            if i % 1 > 1e-4:
                # i is in the middle
                if s[int(i - 0.5)] == s[int(i + 0.5)]:
                    pal = s[int(i - 0.5)] + s[int(i + 0.5)]
                    if len(pal) > len(longest_pal):
                            longest_pal = pal
                    left = int(i - 0.5) - 1
                    right = int(i + 0.5) + 1

                    while left >= 0 and right < len(s) and s[left] == s[right]:
                        pal = s[left] + pal + s[right]
                        if len(pal) > len(longest_pal):
                            longest_pal = pal
                        left -= 1
                        right += 1
            else:
                # i points to a character
                pal = s[int(i)]
                if len(pal) > len(longest_pal):
                    longest_pal = pal
                
                left = int(i) - 1
                right = int(i) + 1

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    pal = s[left] + pal + s[right]
                    if len(pal) > len(longest_pal):
                        longest_pal = pal
                    left -= 1
                    right += 1
            
            i += 0.5
        
        return longest_pal


if __name__ == "__main__":
    test = 'babad'
    solu = Solution()
    print(solu.longestPalindrome(test))