class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        if not intervals:
            return [newInterval]
        
        res = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1
            else:
                res.append(intervals[i])
                i += 1
                break
                
        if res[-1][0] > newInterval[1]:
            # last interval is strictly greater than new interval
            res.insert(len(res) - 1, newInterval)
        elif res[-1][1] >= newInterval[0]:
            res[-1] = [min((res[-1][0], newInterval[0])), 
                       max((res[-1][1], newInterval[1]))]
        else:
            res.append(newInterval)
            
        
        while i < len(intervals):
            if res[-1][1] >= intervals[i][0]:
                res[-1] = [min((res[-1][0], intervals[i][0])),
                          max((res[-1][1], intervals[i][1]))]
            else:
                res.append(intervals[i])
            
            i += 1
                
        return res