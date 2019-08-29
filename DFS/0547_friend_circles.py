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


    def findCircleNum_recursive(self, M) -> int:
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
        
    
    def findCircleNum_iterative(self, M) -> int:
        if M == None or M == [] or M == [[]]:
            return 0

        count = 0
        stack = []

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    count += 1
                    stack.append((i, j))
                    # starts DFS
                    while len(stack) > 0:
                        coor = stack.pop()
                        M[coor[0]][coor[1]] = '#'

                        for idx, candi in enumerate(M[coor[0]]):
                            if candi == 1:
                                stack.append((coor[0], idx))

                        for idx, candi in enumerate([r[coor[1]] for r in M]):
                            if candi == 1:
                                stack.append((idx, coor[1]))

        return count

if __name__ == '__main__':
    solu = Solution()
    print(solu.findCircleNum_iterative([[1,1,0],[1,1,0],[0,0,1]]))