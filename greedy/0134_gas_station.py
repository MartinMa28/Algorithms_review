class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Choose the gas station that could get the most amount of gas in the beginning.
        
        remaining = [gas[i] - cost[i] for i in range(len(gas))]
        
        if sum(remaining) < 0:
            return -1
        
        n = len(remaining)
        remaining = remaining + remaining
        
        start = 0
        cur = 0
        idx = start
        
        while idx < len(remaining):
            if idx - start + 1 == n:
                return start
            
            cur += remaining[idx]
            
            if cur < 0:
                cur = 0
                if start == idx:
                    idx += 1
                    start = idx
                else:
                    start = idx
            else:
                idx += 1
            
        return -1