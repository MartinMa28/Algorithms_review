class Solution:
    def _merge(self, nums1, nums2) -> list:
        if nums1 == []:
            return nums2
        
        if nums2 == []:
            return nums1

        if nums1[0] <= nums2[0]:
            return [nums1[0]] + self._merge(nums1[1:], nums2)
        else:
            return [nums2[0]] + self._merge(nums1, nums2[1:])


    def sortArray_merge_sort(self, nums: list) -> list:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        return self._merge(self.sortArray_merge_sort(nums[:mid]), self.sortArray_merge_sort(nums[mid:]))

    
    def _partition(self, nums: list) -> int:
        """
        Does the parition in place, and returns the true index of pivot.
        """
        pivot = nums[0]

        # i indicates the right end of the smaller part.
        # It begins at the left end of the unsorted array.
        i = 0

        # j is the cursor scans the array from left to right, finding the number
        # that is smaller than pivot.
        for j in range(1, len(nums)):
            if nums[j] <= pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        
        nums[0], nums[i] = nums[i], nums[0]

        return i


    
    def sortArray(self, nums: list) -> list:
        if len(nums) == 1:
            return nums

        pivot_idx = self._partition(nums)

        if len(nums[:pivot_idx]) > 0:
            nums[:pivot_idx] = self.sortArray(nums[:pivot_idx])

        if len(nums[pivot_idx + 1:]) > 0:
            nums[pivot_idx + 1:] = self.sortArray(nums[pivot_idx + 1:])

        return nums[:pivot_idx] + [nums[pivot_idx]] + nums[pivot_idx + 1:]


if __name__ == "__main__":
    solu = Solution()
    #print(solu.sortArray([5, 2, 3, 1]))
    arr = [3, 6, 4, 5, 1, 2, 10, -2, 9, -1]
    solu.sortArray(arr)
    print(arr)