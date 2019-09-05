class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        if len(nums1) > len(nums2):
            longer = nums1
            shorter = nums2
        else:
            longer = nums2
            shorter = nums1

        remaining_nums = {}
        for n in longer:
            remaining_nums[n] = remaining_nums.get(n, 0) + 1

        intersection = []
        for n in shorter:
            if remaining_nums.get(n, 0) > 0:
                intersection.append(n)
                remaining_nums[n] = remaining_nums.get(n) - 1

        return intersection