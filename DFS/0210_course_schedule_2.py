from collections import defaultdict

class Solution:
    
    def _dfs(self, graph, vertex, visiting, visited, stack):
        if vertex in visited:
            return True
        elif vertex in visiting:
            return False
        else:
            visiting.add(vertex)
            
            for neighbor in graph[vertex]:
                if not self._dfs(graph, neighbor, visiting, visited, stack):
                    return False
            
            visiting.discard(vertex)
            visited.add(vertex)
            stack.append(vertex)
            
            return True
                
            
        
    def findOrder(self, numCourses: int, prerq: list) -> list:
        graph = defaultdict(list)
        
        for p in prerq:
            graph[p[1]].append(p[0])
            
        visiting = set()
        visited = set()
        stack = []
        
        for course in range(numCourses):
            if not self._dfs(graph, course, visiting, visited, stack):
                return []
            
        return reversed(stack)
            