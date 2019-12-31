class Solution:
    def _find_smallest(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        if nums[left] < nums[right]:
            return left
        else:
            return right
    
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        smallest_idx = self._find_smallest(nums)
        if target > nums[-1]:
            left = 0
            right = smallest_idx - 1
        else:
            left = smallest_idx
            right = len(nums) - 1
            
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

    def search_one_pass(self, nums: list, target: int) -> int:
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
      
        return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.search([5, 1, 3], 2))