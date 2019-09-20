class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        if matrix[0] == []:
            return False
        else:
            mid_row = len(matrix) // 2
            mid_col = len(matrix[0]) // 2

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                return self.searchMatrix([row[:mid_col] for row in matrix], target) \
                    or self.searchMatrix([row[mid_col:] for row in matrix[:mid_row]], target)
            elif matrix[mid_row][mid_col] < target:
                return self.searchMatrix([row[mid_col + 1:] for row in matrix], target) \
                    or self.searchMatrix([row[0: mid_col + 1] for row in matrix[mid_row + 1:]], target)


if __name__ == "__main__":
    solu = Solution()
    print(solu.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))