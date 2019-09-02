class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) >= len(set2):
            longer = set1
            shorter = set2
        else:
            longer = set2
            shorter = set1

        return [num for num in shorter if num in longer]
