class Solution:
    def _dfs(self, M, row, col) -> None:
        M[row][col] = '#'
        # Only needs to check in one direction because
        # the matrix is symmetrical to the diagonal.
        for idx, candi in enumerate(M[row]):
            if candi == 1:
                self._dfs(M, row, idx)

    
    def findCircleNum(self, M) -> int:
        if M == None or M == [] or M == [[]]:
            return 0

        count = 0
        n = len(M)

        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1:
                    count += 1
                    self._dfs(M, i, j)

        return count
        