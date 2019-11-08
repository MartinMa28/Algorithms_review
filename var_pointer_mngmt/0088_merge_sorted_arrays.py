class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2 == []:
            return nums1
        
        i = len(nums1) - 1
        j = n - 1
        
        while j >= 0 and m - 1 >= 0:
            if nums2[j] >= nums1[m - 1]:
                nums1[i] = nums2[j]
                i -= 1
                j -= 1
            else:
                nums1[i] = nums1[m - 1]
                i -= 1
                m -= 1
        
        if j < 0:
            return
        else:
            while i >= 0:
                nums1[i] = nums2[j]
                i -= 1
                j -= 1
