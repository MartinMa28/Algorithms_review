class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        hs = set()
        for n in nums:
            if n not in hs:
                hs.add(n)
            else:
                return True

        return False