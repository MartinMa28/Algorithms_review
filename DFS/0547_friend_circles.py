class Solution:
    def _dfs(self, M, row, col) -> None:
        M[row][col] = '#'
        
        # check friends horizontally
        for idx, candi in enumerate(M[row]):
            if candi == 1:
                self._dfs(M, row, idx)

        # and then check vertically
        for idx, candi in enumerate([r[col] for r in M]):
            if candi == 1:
                self._dfs(M, idx, col)


    def findCircleNum(self, M) -> int:
        if M == None or M == [] or M == [[]]:
            return 0

        count = 0
        n = len(M)

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    count += 1
                    self._dfs(M, i, j)

        return count
        

if __name__ == '__main__':
    solu = Solution()
    print(solu.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))