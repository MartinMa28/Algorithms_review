class Solution:
    def singleNumber(self, nums: list) -> int:
        h_t = {}

        for n in nums:
            if h_t.get(n):
                h_t.pop(n)
            else:
                h_t[n] = 1

        return h_t.popitem()[0]