from collections import defaultdict

class Solution:
    def __init__(self):
        self.critical_edges = []
        self.discover_time = {}
        self.low_time = {}
    
    def _dfs(self, graph, vertex, parent, cur_time, visited):
        self.discover_time[vertex] = cur_time
        self.low_time[vertex] = cur_time
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor != parent:
                if neighbor not in visited:
                    cur_time + 1
                    self._dfs(graph, neighbor, vertex, cur_time + 1, visited)
                
                self.low_time[vertex] = min((self.low_time[vertex], self.low_time[neighbor]))
                
                if self.discover_time[vertex] < self.low_time[neighbor]:
                    self.critical_edges.append([vertex, neighbor])
                
                              
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # build the adjacent list
        graph = defaultdict(list)
        visited = set()
        
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        self._dfs(graph, 0, -1, 0, visited)
        
        
        return self.critical_edges

if __name__ == "__main__":
    solu = Solution()
    print(solu.single_node_failure(6, [[0, 1], [0, 5], [1, 3], [1, 2], [3, 4], [2, 4], [2, 3]]))