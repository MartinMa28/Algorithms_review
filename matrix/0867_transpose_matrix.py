class Solution:
    def transpose(self, A: list) -> list:
        rows = len(A)
        cols = len(A[0])
        
        transposed = [[None for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = A[i][j]

        return transposed