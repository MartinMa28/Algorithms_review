from collections import defaultdict
import heapq

class Solution:
    
    @staticmethod
    def _dijkstra(graph, start, n, thresh):
        d = [float('inf')] * n
        d[start] = 0
        
        min_heap = [(w, nei) for nei, w in graph[start]]
        heapq.heapify(min_heap)

        while min_heap:
            popped_weight, popped = heapq.heappop(min_heap)
            
            if popped_weight > thresh:
                break
            
            if d[popped] == float('inf'):
                d[popped] = popped_weight
                
                for neighbor, weight in graph[popped]:
                    if d[neighbor] == float('inf'):
                        heapq.heappush(min_heap, (popped_weight + weight, neighbor))
        
        return len(list(filter(lambda x: x <= thresh, d)))
    
        
    
    def findTheCity(self, n: int, edges: list, distanceThreshold: int) -> int:
        graph = defaultdict(list)
        
        for start, end, weight in edges:
            graph[start].append((end, weight))
            graph[end].append((start, weight))
            
        min_con = float('inf')
        min_con_node = -1
        
        for i in range(n):
            con = self._dijkstra(graph, i, n, distanceThreshold)
            print(i, con)
            if con <= min_con:
                min_con = con
                min_con_node = i
        
        return min_con_node
        
                
            
        
if __name__ == "__main__":
    solu = Solution()
    solu.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)