from collections import defaultdict

class Solution:
    
    def _dfs(self, graph, vertex, visiting, visited):
        if vertex in visiting:
            return True
        
        visiting.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if self._dfs(graph, neighbor, visiting, visited):
                    return True
                
        visiting.discard(vertex)
        visited.add(vertex)
        
        return False
                
    
    def canFinish(self, numCourses: int, preq: list) -> bool:
        # build an adjacent list
        graph = defaultdict(list)
        for e in preq:
            graph[e[0]].append(e[1])
            
        visiting = set()
        visited = set()
        
        
        for v in range(numCourses):
            if v in graph and v not in visited:
                if self._dfs(graph, v, visiting, visited):
                    return False
                
        return True


if __name__ == "__main__":
    solu = Solution()

    print(solu.canFinish(2, [[0, 1]]))