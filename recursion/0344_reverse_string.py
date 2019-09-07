class Solution:
    def reverseString(self, s: list) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]


    def _recursive_reverse(self, s: list, up_to: int) -> None:
        if up_to > 0:
            first_item = s.pop(0)
            s.insert(up_to, first_item)
            self._recursive_reverse(s, up_to - 1)

    def reverseString_recursively(self, s: list) -> None:
        self._recursive_reverse(s, len(s) - 1)