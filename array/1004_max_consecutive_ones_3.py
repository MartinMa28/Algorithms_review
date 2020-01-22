from collections import deque

class Solution:
    def longestOnes(self, A: list, K: int) -> int:
        zero_indices = deque()
        i = 0
        ones_len = 0
        max_len = 0
        
        
        while i < len(A):
            if A[i] == 1:
                ones_len += 1
                max_len = max(max_len, ones_len)
            else:
                if len(zero_indices) < K:
                    zero_indices.append(i)
                    ones_len += 1
                    max_len = max(max_len, ones_len)
                elif K > 0:
                    ones_len = i - zero_indices.popleft()
                    zero_indices.append(i)
                else:
                    ones_len = 0
            
            i += 1
        
        return max_len            