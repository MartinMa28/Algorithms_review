from collections import deque

class Solution:
    
    def _bfs(self, v, graph, colors):
        # 0 - blue, 1 - red
        
        queue = deque([v])
        colors[v] = 0
        while len(queue):
            popped = queue.popleft()
            for neighbor in graph[popped]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[popped]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[popped]:
                    return False
                else:
                    # neighbor has the opposite color, valid
                    continue
        
        return True
            
        
    
    def isBipartite(self, edges: list) -> bool:
        graph = {}
        colors = {}
        
        for idx, con in enumerate(edges):
            graph[idx] = con
            
        for v_i in range(len(edges)):
            if len(colors) == len(edges):
                break
            
            if v_i not in colors:
                if not self._bfs(v_i, graph, colors):
                    return False
        
        return True