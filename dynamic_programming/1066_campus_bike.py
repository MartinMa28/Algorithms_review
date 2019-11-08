class Solution:
    def __init__(self):
        self.memo = {}
    
    def _manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def _encode(self, workers, bikes):
        return tuple([tuple([(w[0], w[1]) for w in workers]), tuple([(b[0], b[1]) for b in bikes])])
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        if self._encode(workers, bikes) in self.memo:
            return self.memo[self._encode(workers, bikes)]
        
        if workers == []:
            return 0
        
        min_dist = float('inf')
        for idx, b in enumerate(bikes):
            min_dist = min((min_dist, 
                            self._manhattan(workers[0], b) + self.assignBikes(workers[1:], bikes[:idx] + bikes[idx + 1:])))
        
        
        self.memo[self._encode(workers, bikes)] = min_dist
        return self.memo[self._encode(workers, bikes)]