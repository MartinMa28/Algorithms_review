import heapq

class Solution:
    @staticmethod
    def _on_board(matrix, row, col):
        return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])
    
    def maximumMinimumPath(self, A: list) -> int:
        min_heap = [(-A[0][0], 0, 0)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cur_min = A[0][0]
        visited = set()
        
        while min_heap:
            val, row, col = heapq.heappop(min_heap)
            visited.add((row, col))
            cur_min = min((cur_min, -val))
            
            if row == len(A) - 1 and col == len(A[0]) - 1:
                break
            
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if self._on_board(A, new_row, new_col) and\
                    (new_row, new_col) not in visited:
                    heapq.heappush(min_heap, (-A[new_row][new_col], new_row, new_col))
            
        return cur_min
        

if __name__ == "__main__":
    solu = Solution()
    matrix = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
    print(solu.maximumMinimumPath(matrix))