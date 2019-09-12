class Solution:
    # O(n^2)
    def lengthOfLongestSubstring_slowest(self, s: str) -> int:
        rep = set()
        longest = 0

        for idx in range(len(s)):
            rep.clear()
            cur_idx = idx
            
            while cur_idx < len(s) and s[cur_idx] not in rep:
                rep.add(s[cur_idx])
                cur_idx += 1

            if cur_idx - idx > longest:
                longest = cur_idx - idx

        return longest


    # O(2n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep = set()
        longest = 0
        i = 0
        j = 0

        while i < len(s) and j < len(s):
            if s[j] not in rep:
                rep.add(s[j])
                j += 1
                longest = max(longest, j - i)
            else:
                rep.remove(s[i])
                i += 1

        return longest


    

if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLongestSubstring("abcabc"))
            