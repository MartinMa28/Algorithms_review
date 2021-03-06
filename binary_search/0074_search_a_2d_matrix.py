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
            
            
    # def searchMatrix(self, matrix: list, target: int) -> bool:
    #     if matrix == [] or matrix == [[]]:
    #         return False
        
    #     m = len(matrix)
    #     n = len(matrix[0])
        
    #     mid_row = m // 2
    #     mid_col = n // 2
        
    #     if matrix[mid_row][mid_col] == target:
    #         return True
    #     elif matrix[mid_row][mid_col] > target:
    #         if self._binary_search_1d(matrix[mid_row][:mid_col], target):
    #             return True
    #         else:
    #             return self.searchMatrix(matrix[:mid_row], target)
    #     else:
    #         if self._binary_search_1d(matrix[mid_row][mid_col + 1:], target):
    #             return True
    #         else:
    #             return self.searchMatrix(matrix[mid_row + 1:], target)

    def searchMatrix(self, matrix: list, target: int) -> bool:
        if matrix == None or matrix == [] or matrix == [[]]:
            return False
        
        first_col = [row[0] for row in matrix]
        low = 0
        high = len(first_col) - 1
        
        while low + 1 < high:
            mid = (low + high) // 2
            
            if first_col[mid] > target:
                high = mid - 1
            elif first_col[mid] == target:
                return True
            else:
                low = mid
                
        if first_col[high] <= target:
            row = matrix[high]
        else:
            row = matrix[low]
        
        
        left = 0
        right = len(row) - 1
        
        while left <= right:
            mid = (left + right) >> 1
            
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
            
        return False


if __name__ == "__main__":
    solu = Solution()
    print(solu.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))