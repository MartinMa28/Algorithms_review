class Solution:
    
    def _has_cycle(self, graph, n):
        unvisited = set(range(n))
        visiting = set()
        visited = set()
        
        while len(unvisited) > 0:
            if self._dfs(unvisited, visiting, visited, graph, list(unvisited)[0]):
                return True
        
        return False
    
    def _move_vertex(self, cur_v, source_set, dest_set):
        source_set.discard(cur_v)
        dest_set.add(cur_v)
    
    def _dfs(self, unvisited, visiting, visited, graph, v):
        self._move_vertex(v, unvisited, visiting)
        
        if v in graph:
            for next_v in graph[v]:
                if next_v in visited:
                    continue
                elif next_v in visiting:
                    return True
                else:
                    if self._dfs(unvisited, visiting, visited, graph, next_v):
                        return True
                
        self._move_vertex(v, visiting, visited)
        return False
    
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        # build the graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []
            
        for preq in prerequisites:
            graph[preq[1]].append(preq[0])
            
        
        if self._has_cycle(graph, numCourses):
            return False
        else:
            return True