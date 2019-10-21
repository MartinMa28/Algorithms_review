class Solution:
    def _dfs(self, graph, vertex, visited):
        if not visited[vertex]:
            visited[vertex] = True
        
            for next_v in graph[vertex]:
                self._dfs(graph, next_v, visited)
                
    
    def findCircleNum(self, M) -> int:
        graph = {}
        
        for i in range(len(M)):
            graph[i] = []
            
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1 and i != j:
                    graph[i].append(j)
             
        
        visited = [False] * len(M)
        
        cnt = 0
        for friend in range(len(M)):
            if not visited[friend]:
                cnt += 1
                self._dfs(graph, friend, visited)
                
        return cnt
        
    
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