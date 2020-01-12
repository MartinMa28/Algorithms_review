import heapq

class Solution:
    def assignBikes(self, workers: list, bikes: list) -> list:
        """
        put all pairs into heap
        (man_dist, worker_idx, bike_idx)
        
        worker_set, bike_set
        """
        min_heap = []
        for w_idx, w in enumerate(workers):
            for b_idx, b in enumerate(bikes):
                min_heap.append((abs(w[0] - b[0]) + abs(w[1] - b[1]), w_idx, b_idx))
        
        heapq.heapify(min_heap)
        worker_set = set()
        bike_set = set()
        res = [-1] * len(workers)
        
        while len(worker_set) < len(workers):
            man_dist, w_i, b_i = heapq.heappop(min_heap)
            
            if w_i not in worker_set and b_i not in bike_set:
                res[w_i] = b_i
                worker_set.add(w_i)
                bike_set.add(b_i)
                
        return res
            