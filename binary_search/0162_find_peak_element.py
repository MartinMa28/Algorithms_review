class Solution:
    def _is_peak(self, nums: list, idx: int) -> bool:
        if len(nums) == 1:
            return True
        else:
            if idx == 0:
                if nums[idx] > nums[idx + 1]:
                    return True
                else:
                    return False
            elif idx == len(nums) - 1:
                if nums[idx] > nums[idx - 1]:
                    return True
                else:
                    return False
            else:
                if nums[idx] > nums[idx + 1] and nums[idx] > nums[idx - 1]:
                    return True
                else:
                    return False

    def _dfs(self, nums: list, idx: int) -> int:
        if self._is_peak(nums, idx):
            return idx
        else:
            # check left first
            if idx > 0:
                if nums[idx] < nums[idx - 1]:
                    return self._dfs(nums, idx - 1)
            
            if idx < len(nums) - 1:
                if nums[idx] < nums[idx + 1]:
                    return self._dfs(nums, idx + 1)

    def findPeakElement_slow(self, nums: list) -> int:
        return self._dfs(nums, len(nums) // 2)


    def _find_peak(self, nums: list, left: int, right: int) -> int:
        if left == right:
            return left
        
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return self._find_peak(nums, left, mid)
        elif nums[mid] < nums[mid + 1]:
            return self._find_peak(nums, mid + 1, right)

    def findPeakElement(self, nums: list) -> int:
        return self._find_peak(nums, 0, len(nums) - 1)