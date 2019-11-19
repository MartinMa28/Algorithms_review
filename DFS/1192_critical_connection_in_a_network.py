from collections import defaultdict

class Solution:
    def __init__(self):
        self.cnt = 0
    
    def single_node_failure(self, n: int, connections: list) -> list:
        # build an adjacent graph
        graph = defaultdict(list)
        
        for e in connections:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        visited = set()
        dfn = [-1 for _ in range(n)]
        low = [float('inf') for _ in range(n)]
        parent = [-1 for _ in range(n)]
        children_cnt = [0 for _ in range(n)]
        results = []
        
        for i in range(n):
            if i not in visited:
                self._dfs(i, graph, visited, dfn, low, parent, children_cnt, results)
                
        return results
    
    
    def _dfs(self, vertex, graph, visited, dfn, low, parent, children_cnt, results):
        visited.add(vertex)
        dfn[vertex] = self.cnt
        low[vertex] = self.cnt
        self.cnt += 1
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                parent[neighbor] = vertex
                children_cnt[vertex] += 1
                
                self._dfs(neighbor, graph, visited, dfn, low, parent, children_cnt, results)
                low[vertex] = min((low[vertex], low[neighbor]))
                
                if parent[vertex] == -1:
                    # vertex is the root node
                    if children_cnt[vertex] >= 2:
                        if dfn[vertex] <= low[neighbor]:
                            results.append(vertex)        
                else:
                    if dfn[vertex] <= low[neighbor]:
                        results.append(vertex)
        
            elif neighbor != parent[vertex]:
                # back edge
                low[vertex] = min((low[vertex], low[neighbor]))

if __name__ == "__main__":
    solu = Solution()
    print(solu.single_node_failure(6, [[0, 1], [0, 5], [1, 3], [1, 2], [3, 4], [2, 4], [2, 3]]))