class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        cnt = 0
        for i in range(0, 2 * length - 1):
            if i / 2 % 1 > 0:
                left = i // 2
                right = i // 2 + 1
            else:
                left = i // 2 - 1
                right = i // 2 + 1

            while left >= 0 and right < length:
                if s[left] == s[right]:
                    cnt += 1
                    left -= 1
                    right += 1
                else:
                    break

        return cnt