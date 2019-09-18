class Solution:
    
    def _find_pivot(self, nums, left, right) -> int:
        mid = (left + right) // 2
        if nums[mid] < nums[left]:
            return self._find_pivot(nums, left, mid)
        elif nums[mid] > nums[right]:
            return self._find_pivot(nums, mid + 1, right)
        else:
            return left

    
    def _bi_search(self, nums, target, left, right) -> int:
        if left > right:
            return -1
        else:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self._bi_search(nums, target, left, mid - 1)
            else:
                return self._bi_search(nums, target, mid + 1, right)

    
    def search(self, nums: list, target: int) -> int:
        if nums == []:
            return -1
        
        pivot = self._find_pivot(nums, 0, len(nums) - 1)

        smaller_half = nums[pivot:]
        larger_half = nums[:pivot]

        if target >= smaller_half[0] and target <= smaller_half[-1]:
            found_idx = self._bi_search(smaller_half, target, 0, len(smaller_half) - 1)
            if found_idx >= 0:
                return pivot + found_idx
            else:
                return -1
        else:
            found_idx = self._bi_search(larger_half, target, 0, len(larger_half) - 1)
            if found_idx >= 0:
                return found_idx
            else:
                return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.search([5, 1, 3], 2))