from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        
        for vertex in range(len(graph)):
            if color[vertex] == -1:
                # has not been visited yet
                queue = deque([vertex])
                color[vertex] = 0
                
                while queue:
                    popped = queue.popleft()
                    popped_color = color[popped]
                    
                    for neighbor in graph[popped]:
                        if color[neighbor] == -1:
                            queue.append(neighbor)
                            color[neighbor] = (1 - popped_color)
                        elif color[neighbor] != (1 - popped_color):
                            return False
        
        return True