class Solution:
    def _binary_search_1d(self, nums, target) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
            
            
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        mid_row = m // 2
        mid_col = n // 2
        
        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] > target:
            if self._binary_search_1d(matrix[mid_row][:mid_col], target):
                return True
            else:
                return self.searchMatrix(matrix[:mid_row], target)
        else:
            if self._binary_search_1d(matrix[mid_row][mid_col + 1:], target):
                return True
            else:
                return self.searchMatrix(matrix[mid_row + 1:], target)