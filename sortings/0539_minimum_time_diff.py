from collections import defaultdict

class Solution:
    
    @staticmethod
    def _to_minutes(time_point):
        hours, minutes = time_point.split(':')
        hours = int(hours)
        minutes = int(minutes)
        
        return hours * 60 + minutes
    
    def findMinDifference(self, time_points: list) -> int:
        min_cnt = defaultdict(int)
        
        for tp in time_points:
            min_cnt[self._to_minutes(tp)] += 1
            
        sorted_minutes = []
        
        for minute in range(0, 24 * 60):
            if min_cnt[minute] > 1:
                return 0
            elif min_cnt[minute]:
                sorted_minutes.append(minute)
        
        min_gap = 24 * 60 - sorted_minutes[-1] + sorted_minutes[0]
        
        for i in range(len(sorted_minutes) - 1):
            min_gap = min(sorted_minutes[i + 1] - sorted_minutes[i], min_gap)
            
        return min_gap