from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, K: int) -> int:
        # build an adjacent list
        graph = defaultdict(list)
        
        for e in flights:
            graph[e[0]].append((e[1], e[2]))
            
        visited = set()
        min_dist = defaultdict(dict)
        for i in range(n):
            min_dist[i][0] = float('inf')
            
        min_dist[src][0] = 0
        
        pq = [(0, 0, src)]
        
        while len(pq) > 0:
            cost, k, place = heapq.heappop(pq)
            visited.add(place)
            
            if k > K + 1:
                continue
            
            if place == dst:
                return cost
            
            for neighbor, d in graph[place]:
                if neighbor not in visited and not k + 1 > K + 1:
                    if min_dist[neighbor].get(k + 1, float('inf')) > cost + d:
                        # relaxation
                        min_dist[neighbor][k + 1] = cost + d
                    
                    heapq.heappush(pq, (min_dist[neighbor][k + 1], k + 1, neighbor))
                    
        return -1