import bisect

class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        low = matrix[0][0]
        high = matrix[len(matrix) - 1][len(matrix) - 1]
        
        while low < high:
            mid = (low + high) >> 1
            se_cnt = sum([bisect.bisect_right(row, mid) for row in matrix])
            
            if se_cnt < k:
                low = mid + 1
            else:
                high = mid
                
        return high