class Solution:
    
    def _dfs(self, graph, start, visited):
        if visited[start]:
            return
        else:
            visited[start] = True
        
        for next_v in graph[start]:
            self._dfs(graph, next_v, visited)
    
    def countComponents(self, n: int, edges: list) -> int:
        graph = {}
        for k in range(n):
            graph[k] = []
            
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        visited = [False] * n
        cnt = 0
        
        for v in range(n):
            if not visited[v]:
                cnt += 1
                self._dfs(graph, v, visited)
        
        return cnt