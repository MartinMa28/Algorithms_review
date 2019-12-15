from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        cnt = defaultdict(int)
        
        for n in nums:
            cnt[n] += 1
            
        min_heap = []
        
        for n, freq in cnt.items():
            min_heap.append((-freq, n))
        
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
            
        return res