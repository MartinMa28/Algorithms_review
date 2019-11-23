class Solution:
    
    def _binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = len(nums) - 1
        
        rotated_idx = -1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        rotated_idx = left
        
        if rotated_idx == 0:
            return self._binary_search(nums, 0, len(nums) - 1, target)
        
        if nums[0] <= target and nums[rotated_idx - 1] >= target:
            return self._binary_search(nums, 0, rotated_idx - 1, target)
        elif nums[rotated_idx] <= target and nums[-1] >= target:
            return self._binary_search(nums, rotated_idx, len(nums) - 1, target)
        else:
            return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.search([5, 1, 3], 2))