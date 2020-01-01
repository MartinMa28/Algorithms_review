class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        if not intervals:
            return [newInterval]
        
        res = []
        i = 0
        inserted = False
        
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1
            else:
                break
        
        if i == len(intervals):
            res.append(newInterval)
            return res
        
        left_bound = min((intervals[i][0], newInterval[0]))
        merge_right = False
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            merge_right = True
            i += 1
        
        i -= 1
        if merge_right:
            right_bound = max((intervals[i][1], newInterval[1]))
            res.append([left_bound, right_bound])
            i += 1
        else:
            right_bound = newInterval[1]
            res.append([left_bound, right_bound])
            i += 1
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
       
        return res