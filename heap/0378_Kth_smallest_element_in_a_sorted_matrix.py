import heapq

class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        heap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(heap, matrix[i][j])
        
        res = -1
        
        for _ in range(k):
            res = heapq.heappop(heap)
            
        return res